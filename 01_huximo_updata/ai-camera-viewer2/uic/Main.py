# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 710)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.selectTmpl = QtWidgets.QPushButton(self.centralwidget)
        self.selectTmpl.setGeometry(QtCore.QRect(360, 140, 131, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.selectTmpl.setFont(font)
        self.selectTmpl.setObjectName("selectTmpl")
        self.templete = QtWidgets.QComboBox(self.centralwidget)
        self.templete.setEnabled(True)
        self.templete.setGeometry(QtCore.QRect(30, 70, 461, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.templete.setFont(font)
        self.templete.setObjectName("templete")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(950, 40, 101, 60))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(910, 110, 141, 60))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.okNumber = QtWidgets.QLabel(self.centralwidget)
        self.okNumber.setGeometry(QtCore.QRect(1070, 40, 120, 60))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.okNumber.setFont(font)
        self.okNumber.setStyleSheet("color: rgb(0, 0, 127);")
        self.okNumber.setObjectName("okNumber")
        self.nokNumber = QtWidgets.QLabel(self.centralwidget)
        self.nokNumber.setGeometry(QtCore.QRect(1070, 110, 141, 60))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.nokNumber.setFont(font)
        self.nokNumber.setStyleSheet("color: rgb(0, 0, 127);")
        self.nokNumber.setObjectName("nokNumber")
        self.sysLog = QtWidgets.QTextEdit(self.centralwidget)
        self.sysLog.setEnabled(True)
        self.sysLog.setGeometry(QtCore.QRect(520, 490, 821, 181))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.sysLog.setFont(font)
        self.sysLog.setFocusPolicy(QtCore.Qt.NoFocus)
        self.sysLog.setObjectName("sysLog")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(520, 210, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(520, 460, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.iconStatus = QtWidgets.QLabel(self.centralwidget)
        self.iconStatus.setGeometry(QtCore.QRect(1230, 60, 100, 100))
        self.iconStatus.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.iconStatus.setAutoFillBackground(False)
        self.iconStatus.setText("")
        self.iconStatus.setPixmap(QtGui.QPixmap(":/img/ok_70.8px.png"))
        self.iconStatus.setScaledContents(True)
        self.iconStatus.setObjectName("iconStatus")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(519, 30, 821, 151))
        self.frame.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(60, 40, 101, 60))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.totalNumber = QtWidgets.QLabel(self.frame)
        self.totalNumber.setGeometry(QtCore.QRect(180, 40, 120, 60))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.totalNumber.setFont(font)
        self.totalNumber.setStyleSheet("color: rgb(0, 0, 127);")
        self.totalNumber.setObjectName("totalNumber")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 210, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.markResult = QtWidgets.QTextEdit(self.centralwidget)
        self.markResult.setEnabled(True)
        self.markResult.setGeometry(QtCore.QRect(30, 490, 461, 181))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.markResult.setFont(font)
        self.markResult.setFocusPolicy(QtCore.Qt.NoFocus)
        self.markResult.setObjectName("markResult")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(30, 460, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.iconStatusNok = QtWidgets.QLabel(self.centralwidget)
        self.iconStatusNok.setGeometry(QtCore.QRect(1230, 60, 100, 100))
        self.iconStatusNok.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.iconStatusNok.setAutoFillBackground(False)
        self.iconStatusNok.setText("")
        self.iconStatusNok.setPixmap(QtGui.QPixmap(":/img/nok_70.8px.png"))
        self.iconStatusNok.setScaledContents(True)
        self.iconStatusNok.setObjectName("iconStatusNok")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(520, 240, 821, 211))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tableWidget.setFont(font)
        self.tableWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget.setRowCount(3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(300)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.code2D = QtWidgets.QTextEdit(self.centralwidget)
        self.code2D.setGeometry(QtCore.QRect(30, 280, 451, 171))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.code2D.setFont(font)
        self.code2D.setFocusPolicy(QtCore.Qt.NoFocus)
        self.code2D.setObjectName("code2D")
        self.code2DIn = QtWidgets.QLineEdit(self.centralwidget)
        self.code2DIn.setGeometry(QtCore.QRect(30, 240, 451, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.code2DIn.setFont(font)
        self.code2DIn.setObjectName("code2DIn")
        self.frame.raise_()
        self.selectTmpl.raise_()
        self.templete.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.okNumber.raise_()
        self.nokNumber.raise_()
        self.sysLog.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.iconStatus.raise_()
        self.label_9.raise_()
        self.markResult.raise_()
        self.label_11.raise_()
        self.iconStatusNok.raise_()
        self.tableWidget.raise_()
        self.code2D.raise_()
        self.code2DIn.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 29))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuConfigration = QtWidgets.QMenu(self.menubar)
        self.menuConfigration.setObjectName("menuConfigration")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.action3 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.action3.setFont(font)
        self.action3.setObjectName("action3")
        self.action4 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.action4.setFont(font)
        self.action4.setObjectName("action4")
        self.action5 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.action5.setFont(font)
        self.action5.setObjectName("action5")
        self.action6 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.action6.setFont(font)
        self.action6.setObjectName("action6")
        self.action4_2 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.action4_2.setFont(font)
        self.action4_2.setObjectName("action4_2")
        self.action4_3 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.action4_3.setFont(font)
        self.action4_3.setObjectName("action4_3")
        self.action3_2 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.action3_2.setFont(font)
        self.action3_2.setObjectName("action3_2")
        self.action4_4 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.action4_4.setFont(font)
        self.action4_4.setObjectName("action4_4")
        self.selectTmplCancel = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.selectTmplCancel.setFont(font)
        self.selectTmplCancel.setObjectName("selectTmplCancel")
        self.clearNumber = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.clearNumber.setFont(font)
        self.clearNumber.setObjectName("clearNumber")
        self.action0_3 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.action0_3.setFont(font)
        self.action0_3.setObjectName("action0_3")
        self.menuConfigration.addAction(self.action3)
        self.menuConfigration.addAction(self.action4)
        self.menuConfigration.addAction(self.action6)
        self.menuConfigration.addAction(self.action5)
        self.menuConfigration.addAction(self.action4_2)
        self.menu.addAction(self.action4_3)
        self.menu.addAction(self.action3_2)
        self.menu.addAction(self.action4_4)
        self.menu_2.addAction(self.selectTmplCancel)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.clearNumber)
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menuConfigration.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.selectTmpl.setText(_translate("MainWindow", "确认选中"))
        self.label.setText(_translate("MainWindow", "选择模板"))
        self.label_2.setText(_translate("MainWindow", "合格 "))
        self.label_3.setText(_translate("MainWindow", "不合格  "))
        self.okNumber.setText(_translate("MainWindow", "0"))
        self.nokNumber.setText(_translate("MainWindow", "0"))
        self.label_6.setText(_translate("MainWindow", "历史数据"))
        self.label_7.setText(_translate("MainWindow", "系统日志"))
        self.label_4.setText(_translate("MainWindow", "总数"))
        self.totalNumber.setText(_translate("MainWindow", "0"))
        self.label_9.setText(_translate("MainWindow", "二维码"))
        self.label_11.setText(_translate("MainWindow", "结果"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "时间"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "二维码"))
        self.menuConfigration.setTitle(_translate("MainWindow", "配置"))
        self.menu.setTitle(_translate("MainWindow", "帮助"))
        self.menu_2.setTitle(_translate("MainWindow", "操作"))
        self.action3.setText(_translate("MainWindow", "接口"))
        self.action4.setText(_translate("MainWindow", "模板"))
        self.action5.setText(_translate("MainWindow", "日志"))
        self.action6.setText(_translate("MainWindow", "用户"))
        self.action4_2.setText(_translate("MainWindow", "调试"))
        self.action4_3.setText(_translate("MainWindow", "使用说明"))
        self.action3_2.setText(_translate("MainWindow", "版本"))
        self.action4_4.setText(_translate("MainWindow", "关于"))
        self.selectTmplCancel.setText(_translate("MainWindow", "取消选中"))
        self.clearNumber.setText(_translate("MainWindow", "计数清零"))
        self.action0_3.setText(_translate("MainWindow", "不合格数清零"))

import uic.imagercc_rc