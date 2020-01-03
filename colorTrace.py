import cv2
import numpy as np
import imutils

def color_trace(color_lower, color_upper, img):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # RGB图像转HSV图像
    cv2.imshow('hsv', img_hsv)
    # 创建掩膜，在（color_lower, color_upper）之间的像素设为255，其它为0
    mask = cv2.inRange(img_hsv, color_lower, color_upper)
    cv2.imshow('mask', mask)

    # 腐蚀
    mask_erode = cv2.erode(mask, None, iterations = 2)
    cv2.imshow('erode', mask_erode)
    # 膨胀
    mask_dilate = cv2.dilate(mask_erode, (5, 5), iterations = 2)
    cv2.imshow('dilate', mask_dilate)

    # 高斯滤波
    mask_gaussian = cv2.GaussianBlur(mask_dilate, (3, 3), 0)
    cv2.imshow('mask_gaussian', mask_gaussian)

    # 寻找轮廓
    cnts = cv2.findContours(mask_gaussian.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    #center = None
    print(len(cnts))
    if len(cnts) > 0:
        # 取出最大轮廓
        c = max(cnts, key=cv2.contourArea)
        # 得到物体中心和物体半径
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        # 检测半径大于20像素的物体
        if radius > 20:
            x, y = int(x), int(y)
            # 以物体最小半径画圆
            cv2.circle(img, (x, y), int(radius), (0, 255, 255), 2)
    return img
