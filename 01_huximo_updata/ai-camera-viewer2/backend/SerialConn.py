import serial
import time
from PyQt5.QtCore import QThread, pyqtSignal


class RcvThread(QThread):
    _signal = pyqtSignal(bytes)
    def __init__(self,ser):
        super().__init__()
        self.ser=ser

    def __del__(self):
        self.quit()
        self.wait()

    def run(self):
        while True:
            count = self.ser.inWaiting()
            if count != 0:
                recv = self.ser.read(count)
                print(recv)
                #recv0 = int.from_bytes(recv, byteorder='big', signed=False)
                self._signal.emit(recv)
                self.ser.flushInput()
            time.sleep(0.1)
        self.ser.close()
class SerialConn:
    #初始化串口
    def __init__(self,plcComPort, plcComBaud,plcComData,plcComParity,plcComStop,callback):
        try:
            self.ser = serial.Serial(plcComPort, plcComBaud, plcComData, plcComParity, plcComStop)
            self.ser.flushInput()
            self.thread = RcvThread(self.ser)
            self.thread._signal.connect(callback)
            self.thread.start()
        except Exception as e:
            print(e)
    # 串口发送数据
    def send(self, text):
        try:
            textTmp = chr(text).encode('gbk')
            result = self.ser.write(textTmp)
            print(textTmp)
        except Exception as e:
            print(e)
    #关闭串口
    def close(self):
        try:
            self.thread.__del__()
            self.ser.close()
        except Exception as e:
            print(e)