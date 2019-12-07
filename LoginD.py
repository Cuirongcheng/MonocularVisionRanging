# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginD.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        self.btnregest = QtWidgets.QPushButton(Dialog)
        self.btnregest.setGeometry(QtCore.QRect(250, 440, 261, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.btnregest.setFont(font)
        self.btnregest.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.btnregest.setObjectName("btnregest")
        self.btnlogin = QtWidgets.QPushButton(Dialog)
        self.btnlogin.setGeometry(QtCore.QRect(250, 370, 261, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.btnlogin.setFont(font)
        self.btnlogin.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.btnlogin.setObjectName("btnlogin")
        self.editpwd = QtWidgets.QLineEdit(Dialog)
        self.editpwd.setGeometry(QtCore.QRect(330, 290, 181, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.editpwd.setFont(font)
        self.editpwd.setObjectName("editpwd")
        self.labpwd = QtWidgets.QLabel(Dialog)
        self.labpwd.setGeometry(QtCore.QRect(250, 290, 54, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.labpwd.setFont(font)
        self.labpwd.setObjectName("labpwd")
        self.labuname = QtWidgets.QLabel(Dialog)
        self.labuname.setGeometry(QtCore.QRect(250, 200, 54, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.labuname.setFont(font)
        self.labuname.setObjectName("labuname")
        self.edituname = QtWidgets.QLineEdit(Dialog)
        self.edituname.setGeometry(QtCore.QRect(330, 200, 181, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.edituname.setFont(font)
        self.edituname.setObjectName("edituname")
        self.title = QtWidgets.QLabel(Dialog)
        self.title.setGeometry(QtCore.QRect(150, 100, 511, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(24)
        self.title.setFont(font)
        self.title.setObjectName("title")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btnregest.setText(_translate("Dialog", "注册"))
        self.btnlogin.setWhatsThis(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.btnlogin.setText(_translate("Dialog", "登录"))
        self.labpwd.setText(_translate("Dialog", "密码："))
        self.labuname.setText(_translate("Dialog", "账号："))
        self.title.setText(_translate("Dialog", "基于单目视觉的目标检测与距离测量"))
