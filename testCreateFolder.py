import cv2
import os

# 标定图像保存路径
# photo_path = "./Images./A4"
photo_path = "./Images./test"


# 创建路径
def CreateFolder(path):
    # 去除首位空格
    del_path_space = path.strip()
    # 去除尾部'\'
    del_path_tail = del_path_space.rstrip('\\')
    # 判读输入路径是否已存在
    isexists = os.path.exists(del_path_tail)
    if not isexists:
        os.makedirs(del_path_tail)
        return True
    else:
        return False


# 获取不同角度的标定图像
def gain_photo(photo_path):
    # 检查输入路径是否存在——不存在就创建
    CreateFolder(photo_path)
    # 开启摄像头
    video = cv2.VideoCapture(1)
    # 显示窗口名称
    photo_window = 'calibration'
    # 保存的标定图像名称以数量命名
    photo_num = 0
    while video.isOpened():
        ok, frame = video.read()  # 读一帧的图像
        if not ok:
            break
        else:
            cv2.imshow(photo_window, frame)
            key = cv2.waitKey(10)
            # 按键盘‘A’保存图像
            if key & 0xFF == ord('a'):
                photo_num += 1
                photo_name = photo_path + '\\' + str(photo_num) + '.jpg'
                cv2.imwrite(photo_name, frame)

                print('create photo is :', photo_name)
            # 按键盘‘Q’中断采集
            if key & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break


if __name__ == '__main__':
    gain_photo(photo_path)