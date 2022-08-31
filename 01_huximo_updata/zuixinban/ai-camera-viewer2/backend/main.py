import yaml
import sys
import time
from backend.MSSql import MSSql
from backend.SocketConn import SocketConn
from backend.SerialConn import SerialConn
import backend.StaticParams as par
import logging
import datetime as dt
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QTableWidgetItem, QStyleFactory

from uic.DbChkDialog import Ui_DbChkDialog
from uic.OkNgDialog import Ui_OkNgDialog
from uic.Main import Ui_MainWindow
from uic.SplashPanel import SplashPanel
#log、启动画面
logging.basicConfig(filename="logger.log",level=logging.INFO)
class LogicRun:
    nokNumTmp = 1
    emc_stop = False
    isAuto = False
    def __init__(self,yml_file):
        ui.iconStatus.hide()
        ui.iconStatusNok.hide()
        # 打开yml文件
        try:
            f = open(yml_file, 'r', encoding="utf-8")
            cfg = f.read()
            self.params = yaml.load(cfg, Loader=yaml.FullLoader)
        except Exception as e:
            self.log("读取yml文件失败\n"+str(e))
            return
        else:
            self.log("读取yml文件成功")

        db = self.params.get("interface").get("mssql").get("database")
        host = self.params.get("interface").get("mssql").get("host")
        user = self.params.get("interface").get("mssql").get("user")
        pwd = self.params.get("interface").get("mssql").get("password")
        plcComPort = self.params.get("interface").get("plc").get("com").get("port")
        plcComBaud = self.params.get("interface").get("plc").get("com").get("baud")
        plcComData = self.params.get("interface").get("plc").get("com").get("data")
        plcComStop = self.params.get("interface").get("plc").get("com").get("stop")
        plcComParity = self.params.get("interface").get("plc").get("com").get("parity")
        merliniiIP = self.params.get("interface").get("merlinii").get("socket").get("ip")
        merliniiPort = self.params.get("interface").get("merlinii").get("socket").get("port")
        # 打开数据库连接
        try:
            self.msSql = MSSql(host, user, pwd, db)
            self.refreshTable()
            print()
        except Exception as e:
            self.log("打开数据库失败\n"+str(e))
            return
        else:
            self.log("读取数据库成功")
        # 打开串口
        try:
            self.ser = SerialConn(plcComPort, plcComBaud, plcComData, plcComParity, plcComStop, self.rcvCom)
            self.ser.send(par.AUTO)
            self.ser.send(par.AUTO_CFM)
        except Exception as e:
            self.log("打开PLC串口失败\n"+str(e))
            return
        else:
            self.log("打开PLC串口成功")
        # 连接socket
        try:
            self.skt = SocketConn(merliniiIP, merliniiPort, self.statusSocket)
        except Exception as e:
            self.log("连接打标机失败\n"+str(e))
            return
        else:
            self.log("连接打标机成功")
        # 初始化UI窗口
        ui.templete.addItems(self.params.get("templetes").keys())
        ui.selectTmpl.clicked.connect(lambda: self.enableTempl(False))
        ui.selectTmplCancel.triggered.connect(lambda: self.enableTempl(True))
        ui.clearNumber.triggered.connect(lambda: self.clearNumber())
        ui.code2DIn.returnPressed.connect(lambda: self.textChange())
        dlg.newCodeIn.returnPressed.connect(lambda: self.textChangeDlg())
        f.close()

    #刷新历史数据表格
    def refreshTable(self):
        mktb=self.msSql.ExecQuery("select top 3 MarkDate,MarkText from rv34tmp where DeviceID=6 order by ID desc")
        rn=0
        ui.tableWidget.clearContents()
        while rn < len(mktb):
            itemC1 = QTableWidgetItem(str(mktb[rn][0]))
            itemC2 = QTableWidgetItem(str(mktb[rn][1]))
            ui.tableWidget.setItem(rn,0,itemC1)
            ui.tableWidget.setItem(rn,1,itemC2)
            rn+=1
    #清零
    def clearNumber(self):
        ui.okNumber.setText("0")
        ui.nokNumber.setText("0")
        self.log( "合格数/不合格数清零")
    #合格加1
    def addOK(self):
        ui.iconStatusNok.hide()
        ui.iconStatus.show()
        okNum=int(ui.okNumber.text())
        totalNum=int(ui.totalNumber.text())
        okNum+=1
        totalNum+=1
        ui.okNumber.setText(str(okNum))
        ui.totalNumber.setText(str(totalNum))
        self.ser.send(par.AUTO_OK)
    #不合格加1
    def addNOK(self):
        ui.iconStatusNok.show()
        ui.iconStatus.hide()
        nokNum = int(ui.nokNumber.text())
        totalNum=int(ui.totalNumber.text())
        nokNum += 1
        totalNum += 1
        ui.nokNumber.setText(str(nokNum))
        ui.totalNumber.setText(str(totalNum))
        self.ser.send(par.AUTO_NOK)
    #状态轮询
    def statusSocket(self,hexData,oldHexData):
        print(hexData)
        print(oldHexData)
        if(oldHexData==par.PRINTING and hexData != par.ABORTED):
            if (self.isdbcheck):
                self.showDlg(True)  # 打开复检窗口
                self.ser.send(par.AUTO_OK)
            else:
                self.addOK()
            self.code=""
            ui.code2D.setText("")
        if(hexData == par.OFFLINE):
            self.logtmp("OFFLINE")
        elif(hexData == par.ABORTED):
            self.logtmp("ABORTED")

        elif (hexData == par.ONLINE):
            self.logtmp("ONLINE")
        elif (hexData == par.PRINTING):
            self.logtmp("PRINTING")
        elif (hexData == par.PAUSED):
            self.logtmp("PAUSED")
        elif (hexData == par.PARKING):
            self.logtmp("PARKING")
    #接收来自PLC串口数据
    def rcvCom(self,bytesData):
        print(bytesData)
        print(int.from_bytes(bytesData,'big'))
        hexData =int.from_bytes(bytesData,'big')
        print(self.isAuto)
        print(self.emc_stop)
        #到位信号
        if (hexData == par.ISPOSITION):
            if not self.emc_stop and self.isAuto and not ui.templete.isEnabled() and self.code!="":
                self.skt.sendRsv('G', '')    #到位开始打印
                self.logtmp("零件到位,开始打印")
            else:
                self.logtmp("请确认急停是否按下或是否未扫描")
        elif (hexData == par.EMCSTOP):
            self.emc_stop = True
            self.skt.sendRsv('E', '')    #强制离线
            self.log("急停按下，打标机Offline")
        elif (hexData == par.RESET):
            self.emc_stop = False
            self.isAuto = False
            self.code = ""
            ui.code2D.setText("")
            self.skt.sendRsv('O', '')    #重置在线
            self.ser.send(par.AUTO_CFM)
            self.logtmp("打标机Online")
        elif (hexData == par.SETAUTOOK):
            self.isAuto = True

    #选中模板后禁用防错
    def enableTempl(self,en):
        if(not en):
            ui.code2DIn.setFocus()
            self.curTmpl = ui.templete.currentText()
            src = self.params.get("templetes").get(self.curTmpl).get("src")
            self.length = self.params.get("templetes").get(self.curTmpl).get("static_length")
            self.cont = self.params.get("templetes").get(self.curTmpl).get("static_content")
            self.iscode = self.params.get("templetes").get(self.curTmpl).get("is_code_send")
            self.isdbcheck = self.params.get("templetes").get(self.curTmpl).get("is_db_check_scan")
            self.splits = self.params.get("templetes").get(self.curTmpl).get("split")
            self.skt.sendRsv('P', src)   #set templete
            self.skt.sendRsv('O','')     #online
            self.ser.send(par.TMP_SELECTED)
            self.log( "[选中模板]:"+self.curTmpl)
        ui.templete.setEnabled(en)

    #条码输入
    def textChange(self):
        if (ui.templete.isEnabled()):
            self.logtmp("未选中任何模板")
            self.showOkNgDlg("NG")
            return
        self.code= ui.code2DIn.text()
        ui.code2D.setText(self.code)
        ui.code2DIn.setText("")
        if(len(self.code)!= self.length):
            self.ser.send(par.AUTO_NOK)
            self.logtmp("二维码长度不匹配")
            self.showOkNgDlg("NG")
            return
        if(self.code.find(str(self.cont))<0):
            print(self.code)
            print(self.cont)
            self.ser.send(par.AUTO_NOK)
            self.logtmp("二维码固定内容不匹配")
            self.showOkNgDlg("NG")
            return
        rNum = self.msSql.ExecQuery("select count(ID) from rv34tmp where MarkText='"+self.code+"'")
        print(rNum)
        if(rNum[0][0]>0):
            self.ser.send(par.AUTO_NOK)
            self.logtmp("二维码重复打印")
            self.showOkNgDlg("NG")
            return
        for sl in self.splits.keys():
            field = str(sl).zfill(2)
            sp = self.splits.get(sl)
            val = self.code[sp[0]:sp[1]]
            rsp,dat = self.skt.sendRsv('V', field + val)
            if(rsp):
                self.setResult('第' + field + '行  ' + val +'发送成功')
            else:
                self.ser.send(par.AUTO_NOK)
                self.setResult('第'+field+'行  '+'发送失败')
                self.showOkNgDlg("NG")
                return
        if(self.iscode):
            code_row = self.params.get("templetes").get(self.curTmpl).get("code_row")
            self.setResult('二维码  '+self.code)
            #发送二维码信息
            rspc, datc = self.skt.sendRsv('1', str(code_row).zfill(2) +self.code)
            if(rspc):
                self.setResult('二维码:'+ self.code + '-发送成功')
            else:
                self.setResult('二维码:'+ self.code + '-发送失败')
                self.ser.send(par.AUTO_NOK)
                self.showOkNgDlg("NG")
                return
        if(self.isdbcheck):
            self.setResult('需要复扫')
        print(self.code)
        self.msSql.ExecNonQuery(
            "insert into rv34tmp(MarkDate,MarkText,DeviceID) values(GETDATE(),'" + self.code + "',6)")
        self.refreshTable()
        self.ser.send(par.AUTO_OK)
        self.showOkNgDlg("OK")

    #复检窗口变化
    def textChangeDlg(self):
        newCodeInTmp=dlg.newCodeIn.text()
        dlg.newCode.setText(newCodeInTmp)
        dlg.newCodeIn.setText("")
        if(newCodeInTmp ==dlg.oldCode.toPlainText()):
            dlg.chkResult.setText("OK")
            d.setStyleSheet("background-color: rgb(85, 255, 0);")
            self.setResult("复扫-OK")
            self.showDlg(False)
            self.addOK()
        else:
            d.setStyleSheet("background-color: rgb(255, 0, 0);")
            if(self.nokNumTmp>2):
                self.showDlg(False)
                self.setResult("复扫-NG")
                self.addNOK()
            dlg.DbErrorNum.setText(str(self.nokNumTmp))
            self.nokNumTmp+=1
            dlg.chkResult.setText("NG")

    #弹出复扫窗口
    def showDlg(self,status):
        self.nokNumTmp=0
        try:
            if(status):
                dlg.oldCode.setText(self.code)
                dlg.newCode.setText('')
                dlg.newCodeIn.setText('')
                dlg.newCodeIn.setFocus()
                dlg.chkResult.setText('')
                dlg.DbErrorNum.setText('0')
                d.setStyleSheet("")
                d.open()
            else:
                self.qtimer1 = QTimer()
                self.qtimer1.timeout.connect(self.closeDlg)
                self.qtimer1.start(1000)
        except  Exception as e:
            print(e)
    def closeDlg(self):
        print("closeDlg")
        self.qtimer1.stop()
        d.close()
    def showOkNgDlg(self,text):
        try:
            if(text=="OK"):
                okNgd.setStyleSheet("background-color: rgb(85, 255, 0);")
            elif (text=="NG"):
                okNgd.setStyleSheet("background-color: rgb(255, 0, 0);")
            okNgdlg.OKNGText.setText(text)
            okNgd.open()
            self.qtimer=QTimer()
            self.qtimer.timeout.connect(self.closeOkNgDlg)
            self.qtimer.start(1000)
        except Exception as e:
            print(e)
    def closeOkNgDlg(self):
        self.qtimer.stop()
        okNgd.close()
    #解析二维码结果
    def setResult(self,text):
        now_time = dt.datetime.now().strftime("%H:%M:%S")
        resultText = now_time + "  " + text
        ui.markResult.append(resultText)
        print(resultText)
    #显示暂存日志
    def logtmp(self,text):
        now_time = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logText=now_time+"    "+text
        ui.sysLog.append(logText)
        print(logText)
        return logText
    #保存系统日志
    def log(self,text):
        logging.info(self.logtmp(text))
    def __del__(self):
        print("close")
        self.skt.sendRsv('E', '')  # 强制离线
        self.skt.close()
        self.ser.close()

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def closeEvent(self, *args, **kwargs):
        lgRun.__del__()
        app.exit()
#主函数
if __name__=='__main__':
    app=QApplication(sys.argv)
    print(QStyleFactory.keys())
    splash = SplashPanel()
    app.processEvents()
    w = MyMainWindow()
    d = QDialog()
    okNgd = QDialog()
    ui = Ui_MainWindow()
    dlg = Ui_DbChkDialog()
    okNgdlg = Ui_OkNgDialog()
    ui.setupUi(w)
    dlg.setupUi(d)
    okNgdlg.setupUi(okNgd)
    lgRun=LogicRun("Markware.yml") #/Markware/backend/
    lgRun.log("初始化参数完成")
    w.show()
    splash.finish(w)
    splash.deleteLater()
    sys.exit(app.exec_())
