# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainMenu.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 590)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 0, 621, 60))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lhello = QtWidgets.QLabel(self.centralwidget)
        self.lhello.setGeometry(QtCore.QRect(0, 0, 91, 60))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.lhello.setFont(font)
        self.lhello.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.lhello.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lhello.setObjectName("lhello")
        self.lhello_2 = QtWidgets.QLabel(self.centralwidget)
        self.lhello_2.setGeometry(QtCore.QRect(89, 0, 91, 60))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.lhello_2.setFont(font)
        self.lhello_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.lhello_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lhello_2.setObjectName("lhello_2")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(180, 0, 20, 581))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(7, 55, 791, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.lImg0 = QtWidgets.QLabel(self.centralwidget)
        self.lImg0.setGeometry(QtCore.QRect(200, 79, 290, 321))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.lImg0.setFont(font)
        self.lImg0.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-width: 1px;\n"
"border-style: dotted")
        self.lImg0.setAlignment(QtCore.Qt.AlignCenter)
        self.lImg0.setObjectName("lImg0")
        self.lImg1 = QtWidgets.QLabel(self.centralwidget)
        self.lImg1.setGeometry(QtCore.QRect(500, 79, 290, 321))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.lImg1.setFont(font)
        self.lImg1.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-width: 1px;\n"
"border-style: dotted")
        self.lImg1.setAlignment(QtCore.Qt.AlignCenter)
        self.lImg1.setObjectName("lImg1")
        self.lResult = QtWidgets.QLabel(self.centralwidget)
        self.lResult.setGeometry(QtCore.QRect(200, 409, 601, 131))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.lResult.setFont(font)
        self.lResult.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.lResult.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lResult.setObjectName("lResult")
        self.l21OpenImg = QtWidgets.QPushButton(self.centralwidget)
        self.l21OpenImg.setGeometry(QtCore.QRect(10, 271, 169, 33))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l21OpenImg.sizePolicy().hasHeightForWidth())
        self.l21OpenImg.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.l21OpenImg.setFont(font)
        self.l21OpenImg.setStyleSheet("")
        self.l21OpenImg.setObjectName("l21OpenImg")
        self.l23Shape = QtWidgets.QPushButton(self.centralwidget)
        self.l23Shape.setGeometry(QtCore.QRect(10, 350, 169, 34))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l23Shape.sizePolicy().hasHeightForWidth())
        self.l23Shape.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.l23Shape.setFont(font)
        self.l23Shape.setStyleSheet("")
        self.l23Shape.setObjectName("l23Shape")
        self.l32Depth = QtWidgets.QPushButton(self.centralwidget)
        self.l32Depth.setGeometry(QtCore.QRect(10, 469, 169, 33))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l32Depth.sizePolicy().hasHeightForWidth())
        self.l32Depth.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.l32Depth.setFont(font)
        self.l32Depth.setStyleSheet("")
        self.l32Depth.setObjectName("l32Depth")
        self.l22Color = QtWidgets.QPushButton(self.centralwidget)
        self.l22Color.setGeometry(QtCore.QRect(10, 310, 169, 34))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l22Color.sizePolicy().hasHeightForWidth())
        self.l22Color.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.l22Color.setFont(font)
        self.l22Color.setStyleSheet("")
        self.l22Color.setObjectName("l22Color")
        self.l3DistanceMeasure = QtWidgets.QLabel(self.centralwidget)
        self.l3DistanceMeasure.setGeometry(QtCore.QRect(10, 390, 169, 33))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.l3DistanceMeasure.setFont(font)
        self.l3DistanceMeasure.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.l3DistanceMeasure.setAlignment(QtCore.Qt.AlignCenter)
        self.l3DistanceMeasure.setObjectName("l3DistanceMeasure")
        self.l31OpenImg = QtWidgets.QPushButton(self.centralwidget)
        self.l31OpenImg.setGeometry(QtCore.QRect(10, 429, 169, 34))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l31OpenImg.sizePolicy().hasHeightForWidth())
        self.l31OpenImg.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.l31OpenImg.setFont(font)
        self.l31OpenImg.setStyleSheet("")
        self.l31OpenImg.setObjectName("l31OpenImg")
        self.l33Distance = QtWidgets.QPushButton(self.centralwidget)
        self.l33Distance.setGeometry(QtCore.QRect(10, 508, 169, 34))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l33Distance.sizePolicy().hasHeightForWidth())
        self.l33Distance.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.l33Distance.setFont(font)
        self.l33Distance.setStyleSheet("")
        self.l33Distance.setObjectName("l33Distance")
        self.l11OpenCam = QtWidgets.QPushButton(self.centralwidget)
        self.l11OpenCam.setEnabled(True)
        self.l11OpenCam.setGeometry(QtCore.QRect(10, 113, 169, 33))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l11OpenCam.sizePolicy().hasHeightForWidth())
        self.l11OpenCam.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.l11OpenCam.setFont(font)
        self.l11OpenCam.setStyleSheet("")
        self.l11OpenCam.setAutoRepeatInterval(100)
        self.l11OpenCam.setAutoDefault(False)
        self.l11OpenCam.setDefault(False)
        self.l11OpenCam.setObjectName("l11OpenCam")
        self.l12ImgColl = QtWidgets.QPushButton(self.centralwidget)
        self.l12ImgColl.setGeometry(QtCore.QRect(10, 152, 169, 34))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l12ImgColl.sizePolicy().hasHeightForWidth())
        self.l12ImgColl.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.l12ImgColl.setFont(font)
        self.l12ImgColl.setStyleSheet("")
        self.l12ImgColl.setObjectName("l12ImgColl")
        self.l13SaveImg = QtWidgets.QPushButton(self.centralwidget)
        self.l13SaveImg.setGeometry(QtCore.QRect(10, 192, 169, 33))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l13SaveImg.sizePolicy().hasHeightForWidth())
        self.l13SaveImg.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.l13SaveImg.setFont(font)
        self.l13SaveImg.setStyleSheet("")
        self.l13SaveImg.setObjectName("l13SaveImg")
        self.l1ImageCollect = QtWidgets.QLabel(self.centralwidget)
        self.l1ImageCollect.setGeometry(QtCore.QRect(10, 73, 169, 34))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.l1ImageCollect.setFont(font)
        self.l1ImageCollect.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.l1ImageCollect.setAlignment(QtCore.Qt.AlignCenter)
        self.l1ImageCollect.setObjectName("l1ImageCollect")
        self.l2OptionDetection = QtWidgets.QLabel(self.centralwidget)
        self.l2OptionDetection.setGeometry(QtCore.QRect(10, 231, 169, 34))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.l2OptionDetection.setFont(font)
        self.l2OptionDetection.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.l2OptionDetection.setAlignment(QtCore.Qt.AlignCenter)
        self.l2OptionDetection.setObjectName("l2OptionDetection")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
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
        self.label.setText(_translate("MainWindow", "基于单目视觉的目标检测与距离测量"))
        self.lhello.setText(_translate("MainWindow", "你好，"))
        self.lhello_2.setText(_translate("MainWindow", "用户名"))
        self.lImg0.setText(_translate("MainWindow", "原图像显示"))
        self.lImg1.setText(_translate("MainWindow", "处理图像显示"))
        self.lResult.setText(_translate("MainWindow", "结果显示"))
        self.l21OpenImg.setText(_translate("MainWindow", "打开图像"))
        self.l23Shape.setText(_translate("MainWindow", "形状识别"))
        self.l32Depth.setText(_translate("MainWindow", "轮廓显示"))
        self.l22Color.setText(_translate("MainWindow", "颜色识别"))
        self.l3DistanceMeasure.setText(_translate("MainWindow", "距离测量"))
        self.l31OpenImg.setText(_translate("MainWindow", "打开图像"))
        self.l33Distance.setText(_translate("MainWindow", "距离测量"))
        self.l11OpenCam.setText(_translate("MainWindow", "打开相机"))
        self.l12ImgColl.setText(_translate("MainWindow", "采集图像"))
        self.l13SaveImg.setText(_translate("MainWindow", "保存图像"))
        self.l1ImageCollect.setText(_translate("MainWindow", "图像采集"))
        self.l2OptionDetection.setText(_translate("MainWindow", "目标检测"))
