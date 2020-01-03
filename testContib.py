import cv2
import sys
import numpy as np
import glob

# 标定图像保存路径
photo_path = "./ContibImages"
parameters_path = 'intrinsic_parameters.txt'

# 标定图像
def calibration_photo(photo_path):
    # 设置要标定的角点个数
    x_nums = 8  # x方向上的角点个数
    y_nums = 6
    # 设置(生成)标定图在世界坐标中的坐标
    world_point = np.zeros((x_nums * y_nums, 3), np.float32)  # 生成x_nums*y_nums个坐标，每个坐标包含x,y,z三个元素
    world_point[:, :2] = np.mgrid[:x_nums, :y_nums].T.reshape(-1, 2)  # mgrid[]生成包含两个二维矩阵的矩阵，每个矩阵都有x_nums列,y_nums行
    # .T矩阵的转置
    # reshape()重新规划矩阵，但不改变矩阵元素
    # 保存角点坐标
    world_position = []
    image_position = []
    # 设置角点查找限制
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    # 获取所有标定图
    images = glob.glob(photo_path + '\\*.jpg')
    # print(images)
    for image_path in images:
        image = cv2.imread(image_path)
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        # 查找角点
        ok, corners = cv2.findChessboardCorners(gray, (x_nums, y_nums), None)
        if ok:
            # 把每一幅图像的世界坐标放到world_position中
            world_position.append(world_point)
            # 获取更精确的角点位置
            exact_corners = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
            # 把获取的角点坐标放到image_position中
            image_position.append(exact_corners)
            # 可视化角点
            image = cv2.drawChessboardCorners(image,(x_nums,y_nums),exact_corners,ok)
            cv2.imshow('image_corner',image)
            cv2.waitKey(5000)
    # 计算内参数
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(world_position, image_position, gray.shape[::-1], None, None)
    # 将内参保存起来
    np.savez('./intrinsic_parameters', mtx=mtx, dist=dist)
    print(mtx, dist)
    fw = open("intrinsic_parameters.txt", "w")
    fw.write(("ret:") + str(ret) + "\n")
    fw.write(("mtx:\n") + str(mtx) + "\n")  # 内参数矩阵
    fw.write(("dist:\n") + str(dist) + "\n")  # 畸变系数   distortion cofficients = (k_1,k_2,p_1,p_2,k_3)
    fw.write(("rvecs:\n") + str(rvecs) + "\n")  # 旋转向量  # 外参数
    fw.write(("tvecs:\n") + str(tvecs) + "\n")  # 平移向量  # 外参数
    fw.close()
    # 计算偏差
    mean_error = 0
    for i in range(len(world_position)):
        image_position2, _ = cv2.projectPoints(world_position[i], rvecs[i], tvecs[i], mtx, dist)
        error = cv2.norm(image_position[i], image_position2, cv2.NORM_L2) / len(image_position2)
        mean_error += error
    print("total error: ", mean_error / len(image_position))

# def dispCount(parameters_path):
#     mtx = [[2.21161438e+03,0.00000000e+00,3.05567396e+02][0.00000000e+00,2.54387179e+03,2.49912908e+02][0.00000000e+00,0.00000000e+00,1.00000000e+00]]
#     dist = [[5.16004172e-01,3.25479280e+00,- 1.10713431e-02,- 1.38040231e-02,- 1.97797227e+03]]
#     # 添加点击事件，打印当前点的距离
#     def callbackFunc(e, x, y, f, p):
#         if e == cv2.EVENT_LBUTTONDOWN:
#             print(x, y)
#                 # str1 = ' '
#                 # str2 = str1.join(str(i) for i in threeD[y][x])
#                 # print(threeD[y][x])
#                 # fw = open("result.txt", "w")
#                 # fw.write("匹配点对图像像素坐标：（" + str(x) + ", " + str(y) + ")\n" + "对应特征点三维坐标：" + str2)
#                 # fw.close()
#                 # self.ResultLabel.setText("匹配点对图像像素坐标：（" + str(x) + ", " + str(y) + ")\n" +
#                 #                          "对应特征点三维坐标：（" + str2 + "）")
#
#         while True:
#             # 两个trackbar用来调节不同的参数查看效果
#             num = cv2.getTrackbarPos("num", "depth")
#             blockSize = cv2.getTrackbarPos("blockSize", "depth")
#             if blockSize % 2 == 0:
#                 blockSize += 1
#             if blockSize < 5:
#                 blockSize = 5
#
#             # 根据Block Maching方法生成差异图（opencv里也提供了SGBM/Semi-Global Block Matching算法）
#             stereo = cv2.StereoBM_create(numDisparities=16 * num, blockSize=blockSize)
#             # stereo = cv2.StereoSGBM_create(numDisparities=16 * num, blockSize=blockSize)
#             disparity = stereo.compute(self.imgL, self.imgR)
#
#             disp = cv2.normalize(disparity, disparity, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
#             # 将图片扩展至3d空间中，其z方向的值则为当前的距离
#             threeD = cv2.reprojectImageTo3D(disparity.astype(np.float32) / 16., camera_configs.Q)
#
#             cv2.imshow("depth", disp)
#             key = cv2.waitKey(1)
#             if key == ord("q"):
#                 break
#
#             cv2.setMouseCallback("depth", callbackFunc, None)
#         cv2.destroyAllWindows()

if __name__ == '__main__':
    calibration_photo(photo_path)