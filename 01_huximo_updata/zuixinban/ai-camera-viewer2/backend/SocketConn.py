import socket
import time
from PyQt5.QtCore import QThread, pyqtSignal

import backend.StaticParams as par
class LoopThread(QThread):
    _signal = pyqtSignal(str,str)
    def __init__(self,skn):
        super().__init__()
        self.skn=skn

    def __del__(self):
        self,quit()
        self.wait()

    def run(self):
        while True:
            if(self.skn.sk and self.skn.conn):
                rsp, dat =self.skn.sendRsv('S','')
                if(rsp):
                    if(dat!=self.skn.oldStatus):
                        self._signal.emit(dat,self.skn.oldStatus)
                        self.skn.oldStatus=dat
            time.sleep(0.6)
        self.skn.sk.close()

class SocketConn:
    oldStatus=None
    def __init__(self,ip,port,callback):
        try:
            self.sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sk.bind((ip, port))
            self.sk.listen(5)
            while True:
                self.conn, addr = self.sk.accept()
                if(self.conn and addr):
                    print('Connected by', addr)
                    break
            self.thread = LoopThread(self)
            self.thread._signal.connect(callback)
            self.thread.start()
        except Exception as e:
            print(e)

    def sendRsv(self,type,data):
        try:
            if(self.conn):
                self.conn.send(self.reqFormat(type, data))
                while True:
                    msg = self.conn.recv(1024)
                    if(msg):
                        return self.rspFormat(msg)
        except Exception as e:
            print(e)

    def close(self):
        try:
            self.thread.__del__()
            self.sk.close()
        except Exception as e:
            print(e)

    # Extend Protocol
    def reqFormat(self, type, data):
        bcc = ord(type)
        for a in list(data):
            bcc += ord(a)
        BCC = str(bcc & 0xff)
        reqBytes = [chr(par.SOH), type, chr(par.STX), data, chr(par.ETX), BCC.zfill(3), chr(par.CR)]
        req = "".join(reqBytes)
        return req.encode('gbk')
    def rspFormat(self, msg):
        msgTmp = msg.decode("gbk")
        sta=msgTmp.find(chr(par.ACK)) > 0
        data = msgTmp[msgTmp.find(chr(par.STX)) + 1:msgTmp.find(chr(par.ETX))]
        return sta,data
