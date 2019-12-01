# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 12:24:53 2018
@author: Administrator 在窗口显示摄像头帧
"""

import cv2

clicked = False
# CAMERA_CAPTURE = 'rtsp://admin:abc12345@192.168.1.101:554/h264/ch1/main/av_stream'
CAMERA_CAPTURE = 'rtsp://admin:abc12345@192.168.1.101/mpeg4/ch1/sub/av_stream'


def onMouse(event, x, y, flags, param):
    global clicked
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True


cameraCapture = cv2.VideoCapture(CAMERA_CAPTURE)

cv2.namedWindow('MyWindow')
cv2.setMouseCallback('MyWindow', onMouse)

print('showing camear feed. Click window or press any key to stop')

success, frame = cameraCapture.read()

pathf = 'D:\\ProgramData\\Anaconda3\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_cascade.load(pathf)
count = 0
while success and cv2.waitKey(1) == -1 and not clicked:
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)
    for (x, y, w, h) in faces:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        f = cv2.resize(gray[y:y + h, x:x + w], (200, 200))
        cv2.imwrite('./jm/%s.jpg' % str(count), f)
        count += 1
    cv2.imshow('MyWindow', frame)
    success, frame = cameraCapture.read()

cv2.destroyWindow('MyWindow')
cameraCapture.release()