import sys
import cv2
import numpy as np
import os
import shutil
from shapedetector import ShapeDetector
from colorlabeler import ColorLabeler
import testDistanceOfCircle
import argparse
import imutils

from PyQt5.QtGui import QImage
# import LoginDC
# from LoginDC import MyDialog
from MainMenu import Ui_MainWindow #导入了Ui_MainWindow类
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets

class MyMainWindows(QMainWindow, Ui_MainWindow):   #新建一个类  Ui_MainWindow 为first中的一个类
    def __init__(self,parent=None):
        super(MyMainWindows,self).__init__(parent)
        self.setupUi(self)

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
        self.CAM_NUM = 1  # 为0时表示视频流来自笔记本内置摄像头,外部摄像头为1,2，...
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
        boundaries = [([17, 15, 100], [50, 56, 200]), # 红色
                      ([86, 31, 4], [220, 88, 50]), # 蓝色
                      ([25, 146, 190], [62, 174, 250]), # 黄色
                      ([103, 86, 65], [145, 133, 128])] # 灰色
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
        self.KNOWN_DISTANCE = 16  # 这个距离自己实际测量一下
        self.KNOWN_WIDTH = 4  # 水果的高度
        self.KNOWN_HEIGHT = 4
        image = cv2.imread(self.imgName)
        marker = testDistanceOfCircle.find_marker(image)

    def l33distance(self):
        # image = cv2.imread(self.imgName)
        # focalLength = testDistanceOfCircle.calculate_focalDistance(image)
        # testDistanceOfCircle.calculate_Distance(image, focalLength)
        # cv2.waitKey(0)
        self.lResult.setText("程序调试中……")


if __name__ == "__main__":
    #所有的PyQt5应用必须创建一个应用（Application）对象。
    app = QApplication(sys.argv) #QApplication类管理GUI程序的控制流和主要设置，是基于QWidget的，为此特化了QGuiApplication的一些功能，处理QWidget特有的初始化和结束收尾工作。
    mywin = MyMainWindows()
    mywin.show()
    sys.exit(app.exec_())