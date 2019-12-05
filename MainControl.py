import Main as MM
import ImageCollect as ImgColl
import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
import sys

class parentWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = MM.Ui_MainWindow()
        self.main_ui.setupUi(self)


class childWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = ImgColl.Ui_ImgCollWin()
        self.child.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = parentWindow()
    child = childWindow()

    # 通过toolButton将两个窗体关联
    btn = window.main_ui.btnImageCollect
    btn.clicked.connect(child.show)

    # 显示
    window.show()
    sys.exit(app.exec_())