# from threading import Timer
# import datetime
# # 每隔两秒执行一次任务
# def printHello(self):
#     print('123')
#     t = Timer(2, printHello)
#     t.start()
#
# if __name__ == "__main__":
#     printHello()
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Demo(QWidget):
    count = 0
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 50, 500, 400)
        self.setWindowTitle('QTimer')

        self.list = QListWidget()
        self.label = QLabel('显示当前时间')
        self.start = QPushButton('开始')
        self.end = QPushButton('结束')
        layout = QGridLayout()

        #初始化定时器
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.start.clicked.connect(self.startTimer)
        self.end.clicked.connect(self.endTimer)

        layout.addWidget(self.label,0,0,1,2)
        layout.addWidget(self.start,1,0)
        layout.addWidget(self.end,1,1)
        self.setLayout(layout)

    def showTime(self):
        #获取系统现在的时间
        time = QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss dddd')
        self.label.setText(time)

    def startTimer(self):
        #设置时间间隔并启动定时器
        self.timer.start(1000)
        self.start.setEnabled(False)
        self.end.setEnabled(True)

    def endTimer(self):
        #关闭定时器
        self.timer.stop()
        self.start.setEnabled(True)
        self.end.setEnabled(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Demo()
    form.show()
    sys.exit(app.exec_())

