# coding=utf-8
# 导入相应的pthon包
from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2

# 计算中心点函数
def midpoint(ptA, ptB):
	return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)

# 进行参数配置和解析
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True, help="path to the input image")
# ap.add_argument("-w", "--width", type=float, required=True, help="width of the left-most object in the image (in inches)")
# args = vars(ap.parse_args())

# 读取图片
image = cv2.imread("shapeandcolor.png")
# 执行灰度变换
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 执行高斯滤波
gray = cv2.GaussianBlur(gray, (7, 7), 0)

# 执行Canny边缘检测
edged = cv2.Canny(gray, 50, 100)
# 执行腐蚀和膨胀后处理
edged = cv2.dilate(edged, None, iterations=1)
edged = cv2.erode(edged, None, iterations=1)

# 在边缘映射中寻找轮廓
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# 对轮廓点进行排序
(cnts, _) = contours.sort_contours(cnts)
# 设置显示颜色
colors = ((0, 0, 255), (240, 0, 159), (0, 165, 255), (255, 255, 0), (255, 0, 255))
refObj = None

# 循环遍历每一个轮廓点
for c in cnts:
	# 过滤点太小的轮廓点
	if cv2.contourArea(c) < 100:
		continue

	# 计算最小的外接矩形
	box = cv2.minAreaRect(c)
	box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
	box = np.array(box, dtype="int")

	# 对轮廓点进行排序
	box = perspective.order_points(box)

	# 计算BB的中心点
	cX = np.average(box[:, 0])
	cY = np.average(box[:, 1])


	if refObj is None:
		# 获取4个坐标点并计算中心点坐标
		(tl, tr, br, bl) = box
		(tlblX, tlblY) = midpoint(tl, bl)
		(trbrX, trbrY) = midpoint(tr, br)

		# 计算中心点之间的欧式距离
		D = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))
		# 获取计算结果
		refObj = (box, (cX, cY), D / args["width"])
		continue

	# 绘制轮廓
	orig = image.copy()
	cv2.drawContours(orig, [box.astype("int")], -1, (0, 255, 0), 2)
	cv2.drawContours(orig, [refObj[0].astype("int")], -1, (0, 255, 0), 2)

	# 进行坐标堆叠
	refCoords = np.vstack([refObj[0], refObj[1]])
	objCoords = np.vstack([box, (cX, cY)])

	# 遍历所有的坐标点
	for ((xA, yA), (xB, yB), color) in zip(refCoords, objCoords, colors):
		# 绘制点并连接为直线
		cv2.circle(orig, (int(xA), int(yA)), 5, color, -1)
		cv2.circle(orig, (int(xB), int(yB)), 5, color, -1)
		cv2.line(orig, (int(xA), int(yA)), (int(xB), int(yB)), color, 2)

		# 计算坐标之间的欧式距离并及进行距离转换
		D = dist.euclidean((xA, yA), (xB, yB)) / refObj[2]
		(mX, mY) = midpoint((xA, yA), (xB, yB))
		cv2.putText(orig, "{:.1f}in".format(D), (int(mX), int(mY - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.55, color, 2)

		# 显示结果
		cv2.imshow("Image", orig)
		cv2.waitKey(0)