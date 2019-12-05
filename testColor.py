# coding=utf-8
# 导入python包
import numpy as np
import argparse
import imageio
import cv2

# 设置并解析参数
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", help = "path to the image")
# args = vars(ap.parse_args())

# 读取图片
image = cv2.imread("color.png")
# 定义边界列表 （lower[r, g, b], upper[r, g, b]）
boundaries = [([17, 15, 100], [50, 56, 200]),
              ([86, 31, 4], [220, 88, 50]),
              ([25, 146, 190], [62, 174, 250]),
              ([103, 86, 65], [145, 133, 128])]
img_mask = []
# 循环遍历所有的边界
for (lower, upper) in boundaries:
    # 创建上边界和下边界
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")
    # 在指定边界内查找颜色并应用掩码
    mask = cv2.inRange(image, lower, upper)
    # 进行与操作
    output = cv2.bitwise_and(image, image, mask=mask);
    img_mask.append(output)
    # 显示结果
    cv2.imshow("images", output)
    cv2.waitKey(0)
# imageio.mimsave("mask.gif", img_mask)
