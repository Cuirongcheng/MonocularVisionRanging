import sys
from LoginD import Ui_Dialog #导入了Ui_Dialog类
from MainMenuController import MyMainWindows
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
import pymysql


class MyDialog(QMainWindow, Ui_Dialog):
    def __init__(self):
        super(MyDialog, self).__init__()
        self.setupUi(self)

        # 绑定按钮事件
        self.btnlogin.clicked.connect(self.login)
        self.btnregest.clicked.connect(self.register)

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

    def login(self):
        try:
            """用户登录"""
            uname = self.edituname.text()
            upwd = self.editpwd.text()
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
                self.finaluname = uname
                print("登录成功")
                msgBox = QMessageBox(QMessageBox.Warning, '提示', '登录成功')
                msgBox.exec()
                # self.jumptoMenu()
                print("执行跳转")
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

    def jumptoMenu(self):
        print("显示主菜单界面")
        app = QApplication(sys.argv)
        mywin = MyMainWindows()
        mywin.show()
        # MyMainWindows.setupUi()
        print("进入主菜单界面")
        sys.exit(app.exec_())


if __name__ == "__main__":
    #所有的PyQt5应用必须创建一个应用（Application）对象。
    app = QApplication(sys.argv) #QApplication类管理GUI程序的控制流和主要设置，是基于QWidget的，为此特化了QGuiApplication的一些功能，处理QWidget特有的初始化和结束收尾工作。
    mydialog = MyDialog()
    mydialog.show()
    sys.exit(app.exec_())