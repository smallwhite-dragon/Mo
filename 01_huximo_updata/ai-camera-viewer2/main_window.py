"""
In this example, we demonstrate how to create simple camera viewer using Opencv3 and PyQt5

Author: Berrouba.A
Last edited: 21 Feb 2018
"""
# import system module
import sys
import os
import time
from SplashPanel import SplashPanel
# import some PyQt5 modules
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer, QThread, pyqtSignal
import numpy as np
import requests
# import Opencv module
import cv2
import csv
from infer import getRes,buildDetector
from ui_main_window1111 import *
import json
from threading import Timer


#import paddlex as pdx

url = 'http://10.20.25.145:8899'
getPNInfoByBarcode = url+'/TestingBLL/GetPNWOFlowByBarcode'
saveResultToBIS = url+'/TestingBLL/BlnSaveProductTestingData'

class LoopThread(QThread):
    _signal = pyqtSignal()

    def __init__(self):
        super().__init__()

    def __del__(self):
        self.quit()
        self.wait()

    def run(self):
        while True:
            self._signal.emit()
            #time.sleep(0.6)

class MainWindow(QWidget):
    # class constructor
    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.thread = LoopThread()
        # create a timer
        self.timer = QTimer()
        self.timer_cap = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)
        self.timer_cap.timeout.connect(self.timing_device)
        # set control_bt callback clicked  function
        self.ui.control_bt.clicked.connect(self.controlTimer)
        self.ui.capture_bt.clicked.connect(self.capture)
        self.ui.newcode.returnPressed.connect(lambda: self.textChange())
        self.controlTimer()
        self.ui.newcode.setFocus()
        #self.detector = buildDetector(model_dir='model', threshold=0.9)
        self.detector = None
        self.ui.comboBox.currentTextChanged.connect(self.add_model)
        self.ui.pushButton_reelect.pressed.connect(self.key_power)
        self.select_model()
        #self.ui.pushButton_reelect.connect(self.add_model())
        self._res = None
        self._image = None
        self._image_origin = None
        self.time_flag = False
        self.cam_flag = False

        #????????????
    def select_model(self):
        self.ui.comboBox.addItem('Please select a model')
        for file_name in files:
            #print(file_name)
            self.ui.comboBox.addItem(file_name)

    #????????????????????????
    def add_model(self, trigger_text):
        print('Please add_model')
        if trigger_text == 'Please select a model':
            print('??????????????????')  # ????????????????????????
            self.ui.newcode.setDisabled(True)
            # QMessageBox.information(self, '??????', '?????????????????????', QMessageBox.Yes, QMessageBox.Yes)
        else:
            print(trigger_text)
            model_path = 'D:/36ke/model/' + trigger_text
            model_path_model = 'D:/36ke/model/' + trigger_text + '/infer_cfg.yml'

            # model_path = 'D:/ai-camera-viewer2/model/' + trigger_text
            # model_path_model = 'D:/ai-camera-viewer2/model/' + trigger_text + '/infer_cfg.yml'
            if os.path.exists(model_path_model):    # ------------??????????????????????????????--------------
                self.cam_flag = False
                t1 = time.time()
                self.detector = buildDetector(model_dir=model_path, threshold=0.3, use_gpu=False, run_mode='fluid')
                #------------------??????model????????????-------------------
                getRes(image_file='cp1517162058NG.jpg', detector=self.detector)
                t2 = time.time()
                ms = (t2 - t1) * 1000.0
                print("buildDetector: {} ms per batch image".format(ms))
                self.cam_flag = True
                self.ui.comboBox.setDisabled(True)
                self.ui.newcode.setDisabled(False)
            else:
                print('no model')
                QMessageBox.information(self, '??????', '??????????????????model??????????????????????????????')

    #????????????
    def information_msg(self):
        QMessageBox.information(self, '??????', '?????????????????????', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    #????????????
    def key_power(self):
        self.ui.comboBox.setDisabled(False)
        self.ui.newcode.setDisabled(True)

    # ?????????
    def timing_device(self):
        self.time_flag = True

    # view camera
    def viewCam(self):
        # read image in BGR format
        ret, image = self.cap.read()
        # convert image to RGB format
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.flip(image, -1)
        # print(self.time_flag, self.cam_flag)
        if self.time_flag:
            t1 = time.time()
        if self.detector is not None and self.cam_flag:
            self._image_origin = np.array(image)
            self._res, self._image = getRes(image_file=self._image_origin, detector=self.detector)
            # self._res, self._image = getRes(image_file='D:/36ke/image/cp1628562696NG.jpg', detector=self.detector)
            # print(self._res)
        else:
            self._image = np.copy(image)
        if self.time_flag:
            t2 = time.time()
            ms = (t2 - t1) * 1000.0
            # print("Inference: {} ms per batch image".format(ms))
            self.ui.timems.setText(str(int(ms)))
            self.time_flag = False

        self._image = np.asarray(self._image)
        # get image infos
        height, width, channel = self._image.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(self._image.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
        self.ui.image_label.setPixmap(QPixmap.fromImage(qImg))

    def cap_timer(self):
        self.thread._signal.connect(self.capture)
        self.thread.start()

    def textChange(self):
        print("textChange")
        self.ui.newcode.setFocus()
        self.ui.newcode.selectAll()
        time.sleep(5)    #??????????????????????????????
        self.capture()

    # capture
    def capture(self):
        if self.detector is None:
            print('Detector is None,ples')
        self.ui.okng.setText('NG')
        self.ui.rate.setText('...')
        self.ui.dianchi_num.setText('...')
        self.ui.huximo_num.setText('...')
        if self.timer.isActive():
            image, pg1 = self.infer()

            # ------------------BIS????????????/??????-------------------
            # res01 = 0
            # if pg1 == 'Pass':
            #     res01 = 1
            # self.toBIS(res01)
            # self.toBIS(int(pg1 == 'Pass'))
            image2 = cv2.cvtColor(np.asarray(image), cv2.COLOR_BGR2RGB)      #111111
            t = time.time()
            self.img_str = 'cp' + str(int(t))
            cv2.imwrite("D:\36ke\model" + time.ctime() + pg1 + ".jpg", image2)
            height, width, channel = image.shape
            step = channel * width
            # create QImage from image
            qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
            # show image in img_label
            self.ui.image_label_2.setPixmap(QPixmap.fromImage(qImg))
        else:
            QMessageBox.warning(self, "??????", "??????????????????", QMessageBox.Yes)

    def infer(self):
        # ------????????????????????????-----
        thresh_cov = 0.5
        thresh_hxm = 0.7
        # ------????????????????????????-----

        res = self._res
        image = self._image

        print(res)
        covers = []
        huximos = []
        score = 0.0
        for re in res['boxes']:
            id_class = re[0]
            confd = re[1]
            score += confd      #score
            if id_class == 1 and confd > thresh_cov:
                covers.append(re)
            elif id_class == 0 and confd > thresh_hxm:
                huximos.append(re)
        conts_flag = True
        for hxm in huximos:
            cont_flag = False
            for cov in covers:
                if hxm[2] >= cov[2] and hxm[3] >= cov[3] and hxm[4] <= cov[4] and hxm[5] <= cov[5]:
                    cont_flag = True
                    break
            conts_flag = conts_flag and cont_flag
        print(conts_flag)
        print(len(covers))
        print(len(huximos))
        if (len(covers)+len(huximos)) != 0:
            self.ui.rate.setText(str(int(score*100/(len(covers)+len(huximos))))+'%')
        self.ui.dianchi_num.setText(str(len(covers)))
        self.ui.huximo_num.setText(str(len(huximos)))
        if len(covers) != 0 and len(covers) == len(huximos) and conts_flag:
            pass
        else:
            self.ui.rate.setText('0.0%')
            self.ui.okng.setText('NG')
            pg = 'NG'
            self.ui.okng.setStyleSheet("color:red")
            return self._image, pg
        self.ui.okng.setText('Pass')
        pg = 'Pass'
        self.ui.okng.setStyleSheet("color:green")
        return self._image, pg


    def toBIS(self, result):
        pnInfoRes = None
        code = self.ui.newcode.text()
        print(code)
        payload = {
            "StrSN": code,
            "StrProcName": ""
        }
        print(payload)
        if code is not None and len(code) > 0:
            pnInfoRes = requests.post(url=getPNInfoByBarcode, data=payload)
        print(pnInfoRes.text)
        print(result)
        infotext = json.loads(pnInfoRes.text)
        print(infotext)
        StrPN = infotext['StrPN']
        StrWo = infotext['StrWo']
        StrFlowType = infotext['StrFlowType']
        print(StrPN)
        print(StrWo)
        print(StrFlowType)

        #??????BIS??????
        payload2 = {
            "blnClsMean": False,
            "IntBarChgFlag": 0,
            "IntBarFlag": 0,
            "IntJigStatus": 0,
            "IntMappingFTMerge": 0,
            "IntMappingType": 0,
            "IntPcbFlag": 0,
            "IntProcessLvl": 0,
            "IntRtnCnt": 0,
            "IntTestCnt": 0,
            "IntTestResult": result,
            "IntTestType": 0,
            "IsCheckTwoBarcode": False,
            "IsDvTest": False,
            "IsFirst": False,
            "IsPTL": "Y",
            "StrBarcode": code,
            "StrCellGroup": "",
            "StrChannelNo": "",
            "StrDeviceNo": "NVT-04510",
            "StrErrMsg": "",
            "StrErrorMsg": "",
            "StrFlowType": StrFlowType,
            "StrLineNo": "SMPL",
            "StrLotNo": "",
            "MachineNo": "A4306-1",
            "StrModelNo": "",
            "StrParamValue": "LEN_X=10.1,LEN_Y=10.2",
            "StrPN": StrPN,
            "StrProcName": "FILM-OUTSIDE",
            "StrTestUser": "User",
            "StrWo": StrWo,
            'StrMachineNo': '1'
        }
        res = requests.post(url=saveResultToBIS, data=payload2)
        print(res)
        print(res.text)
        print(type(res.text))
        res_text = json.loads(res.text)
        if res.status_code == 200 and res_text is not None and res_text['ReturnValue']:
            print('BIS????????????')
            self.ui.BIS_okng.setText('BIS????????????')
            self.ui.BIS_okng.setStyleSheet("color:green")
        else:
            print('BIS????????????')
            self.ui.BIS_okng.setText('BIS????????????')
            self.ui.BIS_okng.setStyleSheet("color:red")

    # start/stop timer
    def controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            self.cap = cv2.VideoCapture(1)
            # self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # ????????????
            # self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)  # ????????????
            # start timer
            self.timer.start(100)
            self.timer_cap.start(5000)
            # update control_bt text
            self.ui.control_bt.setText("Stop")
            self.ui.image_label.setText("??????????????????")
        # if timer is started
        else:
            # stop timer
            self.timer.stop()
            self.timer_cap.stop()
            # release video capture
            self.cap.release()
            # update control_bt text
            self.ui.control_bt.setText("Start")
            self.ui.image_label.setText("??????????????????")

    def closeEvent(self, event):
        #self.f.close()
        self.timer.stop()
        self.cap.release()

if __name__ == '__main__':

    path='D:\\36ke\\model\\'     #------------??????????????????????????????--------------
    # path='D:\\ai-camera-viewer2\\model'
    files = os.listdir(path)
    app = QApplication(sys.argv)
    splash = SplashPanel()
    app.processEvents()
    # create and show mainWindow
    mainWindow = MainWindow()
    mainWindow.showMaximized()
    splash.finish(mainWindow)
    splash.deleteLater()
    sys.exit(app.exec_())
