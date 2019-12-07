# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 601)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(140, 80, 511, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(24)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.btnImageCollect = QtWidgets.QPushButton(self.centralwidget)
        self.btnImageCollect.setGeometry(QtCore.QRect(90, 280, 151, 51))
        self.btnImageCollect.setObjectName("btnImageCollect")
        self.btnTargetDetection = QtWidgets.QPushButton(self.centralwidget)
        self.btnTargetDetection.setGeometry(QtCore.QRect(320, 280, 151, 51))
        self.btnTargetDetection.setObjectName("btnTargetDetection")
        self.btnDistanceMeasure = QtWidgets.QPushButton(self.centralwidget)
        self.btnDistanceMeasure.setGeometry(QtCore.QRect(540, 280, 151, 51))
        self.btnDistanceMeasure.setObjectName("btnDistanceMeasure")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "基于单目视觉的目标检测与距离测量"))
        self.btnImageCollect.setText(_translate("MainWindow", "图像采集"))
        self.btnTargetDetection.setText(_translate("MainWindow", "目标检测"))
        self.btnDistanceMeasure.setText(_translate("MainWindow", "距离测量"))
