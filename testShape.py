# # coding=utf-8
# # 导入python包
# import cv2
#
# # 读取彩色图片
# img = cv2.imread('./Images/1.bmp')
# # 转换为灰度图片
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # 进行二值化处理
# ret,binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
#
# # 寻找轮廓
# contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#
# # 绘制不同的轮廓
# draw_img0 = cv2.drawContours(img.copy(),contours,0,(0,255,255),3)
# draw_img1 = cv2.drawContours(img.copy(),contours,1,(255,0,255),3)
# draw_img2 = cv2.drawContours(img.copy(),contours,2,(255,255,0),3)
# draw_img3 = cv2.drawContours(img.copy(),contours,-1,(0,0,255),3)
#
# # 打印结果
# print ("contours:类型：",type(contours))
# print ("第0 个contours:",type(contours[0]))
# print ("contours 数量：",len(contours))
#
# print ("contours[0]点的个数：",len(contours[0]))
# print ("contours[1]点的个数：",len(contours[1]))
#
# # 显示并保存结果
# cv2.imshow("img", img)
# cv2.imshow("draw_img0", draw_img0)
# cv2.imshow("draw_img1", draw_img1)
# cv2.imshow("draw_img2", draw_img2)
# # cv2.imwrite("rect_result.png", draw_img3)
# cv2.imshow("draw_img3", draw_img3)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import  cv2


def otsu_seg(img):

    ret_th, bin_img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    return ret_th, bin_img

def find_pole(bin_img):
    contours, hierarchy = cv2.findContours(bin_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    area = 0
    for i in range(len(contours)):
        area += cv2.contourArea(contours[i])
    area_mean = area / len(contours)
    mark = []
    for i in range(len(contours)):
        if cv2.contourArea(contours[i]) < area_mean:
            mark.append(i)

    return img, contours, hierarchy, mark

def draw_box(img,contours):
    img = cv2.rectangle(img,
                  (contours[0][0], contours[0][1]),
                  (contours[1][0], contours[1][1]),
                  (255,255,255),
                  3)
    return img

def main(img):
    ret, th = otsu_seg(img)
    img_new, contours, hierarchy, mark = find_pole(th)
    for i in range(len(contours)):
        if i not in mark:
            left_point = contours[i].min(axis=1).min(axis=0)
            right_point = contours[i].max(axis=1).max(axis=0)
            img = draw_box(img, (left_point, right_point))
    return img


if __name__ =="__main__":
    img = cv2.imread('shapeandcolor.png')
    cv2.imshow("img", img)
    cv2.waitKey(0)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 视频色彩转换回RGB，这样才是现实的颜色
    cv2.imshow("img", gray)
    cv2.waitKey(0)
    img = main(gray)
    cv2.imshow("img",img)
    # cv2.imwrite('G:/test_d.png', img)
