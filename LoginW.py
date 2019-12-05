# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginW.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.edituname = QtWidgets.QLineEdit(Form)
        self.edituname.setGeometry(QtCore.QRect(340, 220, 181, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.edituname.setFont(font)
        self.edituname.setObjectName("edituname")
        self.btnregest = QtWidgets.QPushButton(Form)
        self.btnregest.setGeometry(QtCore.QRect(260, 460, 261, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.btnregest.setFont(font)
        self.btnregest.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.btnregest.setObjectName("btnregest")
        self.labpwd = QtWidgets.QLabel(Form)
        self.labpwd.setGeometry(QtCore.QRect(260, 310, 54, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.labpwd.setFont(font)
        self.labpwd.setObjectName("labpwd")
        self.btnlogin = QtWidgets.QPushButton(Form)
        self.btnlogin.setGeometry(QtCore.QRect(260, 390, 261, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.btnlogin.setFont(font)
        self.btnlogin.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.btnlogin.setObjectName("btnlogin")
        self.title = QtWidgets.QLabel(Form)
        self.title.setGeometry(QtCore.QRect(160, 120, 511, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(24)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.editpwd = QtWidgets.QLineEdit(Form)
        self.editpwd.setGeometry(QtCore.QRect(340, 310, 181, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.editpwd.setFont(font)
        self.editpwd.setObjectName("editpwd")
        self.editpwd.setEchoMode(QLineEdit.Password)
        self.labuname = QtWidgets.QLabel(Form)
        self.labuname.setGeometry(QtCore.QRect(260, 220, 54, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.labuname.setFont(font)
        self.labuname.setObjectName("labuname")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btnregest.setText(_translate("Form", "注册"))
        self.labpwd.setText(_translate("Form", "密码："))
        self.btnlogin.setText(_translate("Form", "登录"))
        self.title.setText(_translate("Form", "基于单目视觉的目标检测与距离测量"))
        self.labuname.setText(_translate("Form", "账号："))
