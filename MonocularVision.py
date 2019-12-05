import sys
import cv2
import numpy as np
import os
import shutil

from PyQt5.QtCore import pyqtSignal

from shapedetector import ShapeDetector
from colorlabeler import ColorLabeler
import argparse
import imutils
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QApplication, QMessageBox, QLineEdit
from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql


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
        self.l23Shape.setText(_translate("MainWindow", "形状检测"))
        self.l32Depth.setText(_translate("MainWindow", "深度估计"))
        self.l22Color.setText(_translate("MainWindow", "颜色检测"))
        self.l3DistanceMeasure.setText(_translate("MainWindow", "距离测量"))
        self.l31OpenImg.setText(_translate("MainWindow", "打开图像"))
        self.l33Distance.setText(_translate("MainWindow", "距离测量"))
        self.l11OpenCam.setText(_translate("MainWindow", "打开相机"))
        self.l12ImgColl.setText(_translate("MainWindow", "采集图像"))
        self.l13SaveImg.setText(_translate("MainWindow", "保存图像"))
        self.l1ImageCollect.setText(_translate("MainWindow", "图像采集"))
        self.l2OptionDetection.setText(_translate("MainWindow", "目标检测"))

        self.c = 1;
        # self.lhello_2.setText(str(MyDialog.finaluname))

        # 绑定按钮事件
        # 图像采集功能模块
        self.l11OpenCam.clicked.connect(self.l11openCam)
        self.l12ImgColl.clicked.connect(self.l12imgColl)
        self.l13SaveImg.clicked.connect(self.l13saveImg)
        # # 目标检测功能模块
        self.l21OpenImg.clicked.connect(self.l21openImg)
        self.l22Color.clicked.connect(self.l22color)
        self.l23Shape.clicked.connect(self.l23shape)
        # # 距离测量功能模块
        self.l31OpenImg.clicked.connect(self.l21openImg)
        self.l32Depth.clicked.connect(self.l32depth)
        self.l33Distance.clicked.connect(self.l33distance)

    def l11openCam(self):
        self.timer_camera = QtCore.QTimer()  # 定义定时器，用于控制显示视频的帧率
        self.cap = cv2.VideoCapture()  # 视频流
        self.CAM_NUM = 0  # 为0时表示视频流来自笔记本内置摄像头,外部摄像头为1,2，...
        if self.timer_camera.isActive() == False:  # 若定时器未启动
            flag = self.cap.open(self.CAM_NUM)  # 参数是0，表示打开笔记本的内置摄像头，参数是视频文件路径则打开视频
            if flag == False:  # flag表示open()成不成功
                msg = QtWidgets.QMessageBox.warning(self, 'warning', "请检查相机于电脑是否连接正确", buttons=QtWidgets.QMessageBox.Ok)
            else:
                self.timer_camera.start(30)  # 定时器开始计时30ms，结果是每过30ms从摄像头中取一帧显示
                self.l11OpenCam.setText('关闭相机')
        else:
            self.timer_camera.stop()  # 关闭定时器
            self.cap.release()  # 释放视频流
            self.lImg0.clear()  # 清空视频显示区域
            self.l11OpenCam.setText('打开相机')
        self.timer_camera.timeout.connect(self.show_camera)  # 若定时器结束，则调用show_camera()

    def show_camera(self):
        flag, self.image = self.cap.read()  # 从视频流中读取

        show = cv2.resize(self.image, (640, 480))  # 把读到的帧的大小重新设置为 640x480
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)  # 视频色彩转换回RGB，这样才是现实的颜色
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0],
                                 QtGui.QImage.Format_RGB888)  # 把读取到的视频数据变成QImage形式
        self.lImg0.setPixmap(QtGui.QPixmap.fromImage(showImage))  # 往显示视频的Label里 显示QImage

    def l12imgColl(self):
        flag, self.image = self.cap.read()  # 从视频流中读取

        show = cv2.resize(self.image, (640, 480))  # 把读到的帧的大小重新设置为 640x480
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)  # 视频色彩转换回RGB，这样才是现实的颜色
        self.showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0],
                                      QtGui.QImage.Format_RGB888)  # 把读取到的视频数据变成QImage形式
        self.lImg1.setPixmap(QtGui.QPixmap.fromImage(self.showImage))  # 往显示视频的Label里 显示QImage

    def l13saveImg(self):
        # 保存图像
        flag, self.image = self.cap.read()  # 从视频流中读取
        show = cv2.resize(self.image, (640, 480))  # 把读到的帧的大小重新设置为 640x480
        cv2.imshow("img", show)
        self.imgSave = './Images/' + str(self.c) + '.bmp'
        cv2.imwrite(self.imgSave, show)
        self.c = self.c + 1
        self.lResult.setText("图像保存成功！\n""图像保存路径：\n" + str(self.imgSave))

        '''文件夹形式保存图像，未成功
        fname = QFileDialog.getSaveFileName(
            self, '打开文件', './Image' + str(self.c) + '.bmp', ("Images (*.bmp *.jpg *.tif *.raw)"))
        filename = os.path.basename(fname[0])  # 获取到需要存储的文件名
        print(filename)
        pathname = os.path.join(os.getcwd())    # 获取文件路径
        pathandfilename = os.path.join(os.getcwd(), filename)  # 获取带有文件名的文件路径
        print(pathname)
        print(pathandfilename)
        # newfile = '\\'.join(fname[0].split('/')[:-1])  # 需要存储到的新文件夹
        cv2.imwrite(pathname, show)  # 将图片保存下来
        # if (newfile != os.getcwd()):  # 将图片移动到指定文件夹下
        #     try:
        #         shutil.move(pathname, newfile)
        #     except:
        #         os.unlink(os.path.join(newfile, filename))
        #         shutil.move(pathname, newfile)
        self.c = self.c + 1
        self.lResult.setText("图像保存成功！\n""图像保存路径：\n" + pathandfilename)
        '''

    def l21openImg(self):
        if self.timer_camera.isActive() == True:  # 若定时器未启动
            self.timer_camera.stop()  # 关闭定时器
            self.cap.release()  # 释放视频流
            self.lImg0.clear()  # 清空视频显示区域
        self.imgName, self.imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.bmp;;*.jpg;;*.png;;All Files(*)")
        print(self.imgName)
        # image = cv2.imread(self.imgName)
        # cv2.imshow("images", image)
        self.img0 = QtGui.QPixmap(self.imgName).scaled(640, 480)
        self.lImg0.setPixmap(self.img0)
        self.lResult.setText("图像打开成功！\n""图像打开路径：\n" + str(self.imgName))

    def l22color(self):
        # 读取图片
        image = cv2.imread(self.imgName)
        cv2.imshow("images", image)
        # 定义边界列表 （lower[r, g, b], upper[r, g, b]）
        boundaries = [([17, 15, 100], [50, 56, 200]),  # 红色
                      ([86, 31, 4], [220, 88, 50]),  # 蓝色
                      ([25, 146, 190], [62, 174, 250]),  # 黄色
                      ([103, 86, 65], [145, 133, 128])]  # 灰色
        img_mask = []
        print("开始遍历边界")
        # 循环遍历所有的边界
        for (lower, upper) in boundaries:
            # 创建上边界和下边界
            lower = np.array(lower, dtype="uint8")
            upper = np.array(upper, dtype="uint8")
            print("开始查找颜色")
            # 在指定边界内查找颜色并应用掩码
            mask = cv2.inRange(image, lower, upper)
            # 进行与操作
            output = cv2.bitwise_and(image, image, mask=mask);
            img_mask.append(output)
            # 显示结果
            cv2.imshow("images", output)
            cv2.waitKey(0)
            print("Label显示结果")
            show = cv2.resize(output, (640, 480))  # 把读到的帧的大小重新设置为 640x480
            # show = cv2.resize(output, (self.lImg1.width(), self.lImg1.height()))  # 把读到的帧的大小重新设置为 640x480
            self.showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0],
                                          QtGui.QImage.Format_RGB888)  # 把读取到的视频数据变成QImage形式
            self.lImg1.setPixmap(QtGui.QPixmap.fromImage(self.showImage))  # 往显示视频的Label里 显示QImage

    def l23shape(self):
        # 读取图片
        image = cv2.imread(self.imgName)
        cv2.imshow("images", image)
        # 进行裁剪操作
        resized = imutils.resize(image, width=300)
        ratio = image.shape[0] / float(resized.shape[0])

        # 进行高斯模糊操作
        blurred = cv2.GaussianBlur(resized, (5, 5), 0)
        # 进行图片灰度化
        gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
        # 进行颜色空间的变换
        lab = cv2.cvtColor(blurred, cv2.COLOR_BGR2LAB)
        # 进行阈值分割
        thresh = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY)[1]
        cv2.imshow("Thresh", thresh)

        # 在二值图片中寻找轮廓
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)

        # 初始化形状检测器和颜色标签
        sd = ShapeDetector()
        cl = ColorLabeler()

        # 遍历每一个轮廓
        for c in cnts:
            # 计算每一个轮廓的中心点
            M = cv2.moments(c)
            cX = int((M["m10"] / M["m00"]) * ratio)
            cY = int((M["m01"] / M["m00"]) * ratio)

            # 进行颜色检测和形状检测
            shape = sd.detect(c)
            color = cl.label(lab, c)

            # 进行坐标变换
            c = c.astype("float")
            c *= ratio
            c = c.astype("int")
            text = "{} {}".format(color, shape)
            # 绘制轮廓并显示结果
            cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
            cv2.putText(image, text, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

            cv2.imshow("Image", image)
            cv2.waitKey(0)
            show = cv2.resize(image, (640, 480))  # 把读到的帧的大小重新设置为 640x480
            show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)  # 视频色彩转换回RGB，这样才是现实的颜色
            self.showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0],
                                          QtGui.QImage.Format_RGB888)  # 把读取到的视频数据变成QImage形式
            self.lImg1.setPixmap(QtGui.QPixmap.fromImage(self.showImage))  # 往显示视频的Label里 显示QImage

    def l32depth(self):
        self.lResult.setText("双目视觉利用视差形成深度图功能比较完善，单目深度估计功能开发中，敬请期待……")

    def l33distance(self):
        self.lResult.setText("单目测距功能开发中，敬请期待……")
        # jumptoMenu()

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

        # 绑定按钮事件
        self.btnlogin.clicked.connect(self.check_login)
        self.btnregest.clicked.connect(self.register)

    # 安全登录信号，传出两个参数，密码和账号
    check_login_signal = pyqtSignal(str, str)
    def check_login(self):
        uname = self.edituname.text()
        upwd = self.editpwd.text()
        # 发射信号
        print("sended")
        self.check_login_signal.emit(uname, upwd)

    def register(self):
        """用户注册"""
        try:
            uname = self.edituname.text()
            upwd = self.editpwd.text()
            if not 6 <= len(upwd) <= 10:
                print('请输入6到10位的密码')
                msgBox = QMessageBox(QMessageBox.Warning, '提示', '请输入6到10位的密码!')
                msgBox.exec()
            # 打开与数据库的连接
            conn = pymysql.connect(host="localhost", port=3306, user="root", password="123456",
                                   database="monoculardata",
                                   charset="utf8")
            cur = conn.cursor()
            # 判断用户名是否存在
            sql = 'select count(*) from users where uname = %s'
            # params = [uname]
            cur.execute(sql, (uname,))
            result = cur.fetchone()
            if result[0]:
                print('用户名已经存在，请重新注册')
                msgBox = QMessageBox(QMessageBox.Warning, '提示', '用户名已经存在，请重新注册!')
                msgBox.exec()
            else:
                # 用户名不存在
                sql = 'insert into users(uname, upwd) values(%s, %s)'
                # params = [uname, upwd]
                result = cur.execute(sql, (uname, upwd))
                conn.commit()
                if result == 1:
                    print('注册成功')
                    msgBox = QMessageBox(QMessageBox.Warning, '提示', '注册成功!')
                    msgBox.exec()
                else:
                    print('注册失败')
                    msgBox = QMessageBox(QMessageBox.Warning, '提示', '注册失败!')
                    msgBox.exec()
        except Exception as e:
            print('注册失败，原因是：%s' % e)
            msgBox = QMessageBox(QMessageBox.Warning, '提示', '注册失败，原因是：%s' % e)
            msgBox.exec()
        finally:
            cur.close()
            conn.close()
    #
    # def login(self):
    #     try:
    #         self.flag = 0
    #         """用户登录"""
    #         uname = self.edituname.text()
    #         upwd = self.editpwd.text()
    #         print(uname)
    #         print(upwd)
    #         # 1 连接数据库
    #         conn = pymysql.connect(host="localhost", port=3306, user="root", password="123456",
    #                                database="monoculardata",
    #                                charset="utf8")
    #         #  得到一个游标对象
    #         cs1 = conn.cursor()
    #         # 2, 执行sql语句
    #         sql = """select upwd from users where uname = %s """
    #         cs1.execute(sql, (uname,))
    #         result = cs1.fetchone()
    #         if result == None:
    #             print("用户名错误，登录失败")
    #             msgBox = QMessageBox(QMessageBox.Warning, '提示', '用户名错误，登录失败')
    #             msgBox.exec()
    #         elif result[0] == upwd:
    #             self.finaluname = uname
    #             print("登录成功")
    #             msgBox = QMessageBox(QMessageBox.Warning, '提示', '登录成功')
    #             msgBox.exec()
    #             self.flag = 1;
    #             print("执行跳转")
    #             print(self.flag)
    #             return self.flag, self.finaluname
    #         else:
    #             print("密码错误，登录失败")
    #             msgBox = QMessageBox(QMessageBox.Warning, '提示', '密码错误，登录失败')
    #             msgBox.exec()
    #     except Exception as e:
    #         print("登录失败，失败原因为：%s" % e)
    #         msgBox = QMessageBox(QMessageBox.Warning, '提示', '注册失败，原因是：%s' % e)
    #         msgBox.exec()
    #     finally:
    #         # 关闭
    #         cs1.close()
    #         conn.close()
    #         return self.flag, self.finaluname

class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)


class MyForm(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super(MyForm, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MyWindow()
    ex = MyForm()
    ex.show()

    def check_login(uname,upwd):
        try:
            """用户登录"""
            print(uname)
            print(upwd)
            # 1 连接数据库
            conn = pymysql.connect(host="localhost", port=3306, user="root", password="123456",
                                   database="monoculardata",
                                   charset="utf8")
            #  得到一个游标对象
            cs1 = conn.cursor()
            # 2, 执行sql语句
            sql = """select upwd from users where uname = %s """
            cs1.execute(sql, (uname,))
            result = cs1.fetchone()
            if result == None:
                print("用户名错误，登录失败")
                msgBox = QMessageBox(QMessageBox.Warning, '提示', '用户名错误，登录失败')
                msgBox.exec()
            elif result[0] == upwd:
                print("登录成功")
                msgBox = QMessageBox(QMessageBox.Warning, '提示', '登录成功')
                msgBox.exec()
                print("执行跳转")
                ui.show()
                ui.lhello_2.setText(uname)
            else:
                print("密码错误，登录失败")
                msgBox = QMessageBox(QMessageBox.Warning, '提示', '密码错误，登录失败')
                msgBox.exec()
        except Exception as e:
            print("登录失败，失败原因为：%s" % e)
            msgBox = QMessageBox(QMessageBox.Warning, '提示', '注册失败，原因是：%s' % e)
            msgBox.exec()
        finally:
            # 关闭
            cs1.close()
            conn.close()

    # def changeUname(uname,upwd):
    #     print(uname,upwd)
    #     ui.lhello_2.setText(uname)