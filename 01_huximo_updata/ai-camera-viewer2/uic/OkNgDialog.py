# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OkNgDialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_OkNgDialog(object):
    def setupUi(self, OkNgDialog):
        OkNgDialog.setObjectName("OkNgDialog")
        OkNgDialog.resize(700, 500)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        OkNgDialog.setFont(font)
        self.OKNGText = QtWidgets.QLabel(OkNgDialog)
        self.OKNGText.setGeometry(QtCore.QRect(60, 80, 591, 311))
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.OKNGText.setFont(font)
        self.OKNGText.setAlignment(QtCore.Qt.AlignCenter)
        self.OKNGText.setObjectName("OKNGText")

        self.retranslateUi(OkNgDialog)
        QtCore.QMetaObject.connectSlotsByName(OkNgDialog)

    def retranslateUi(self, OkNgDialog):
        _translate = QtCore.QCoreApplication.translate
        OkNgDialog.setWindowTitle(_translate("OkNgDialog", "状态框"))
        self.OKNGText.setText(_translate("OkNgDialog", "OK"))

