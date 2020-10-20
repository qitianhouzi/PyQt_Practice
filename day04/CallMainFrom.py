# -*- coding: utf-8 -*-

"""
@File    : CallMainFrom.py
@Time    : 2020/10/20 20:44
@Author  : sun
@Email   : 763224955@qq.com
@Software: PyCharm
"""
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QFileDialog
from MainForm import Ui_MianWindow

class MainFrom(QMainWindow,Ui_MianWindow):
    def __init__(self):
        super(MainFrom, self).__init__()
        self.setupUi(self)
        # 菜单的点击事件,当点击关闭菜单时连接槽函数 close()
        self.actionfileCloseFile.triggered.connect(self.close)
        # 菜单的点击事件,当点击关闭时单时连接槽函数 openMsg()
        self.fileOpenAction.triggered.connect(self.openMsg)

    def openMsg(self):
        file,ok = QFileDialog.getOpenFileName(self,"打开","c:/","All Files(*);;Text Files")
        # 在状态栏显示文件地址
        self.statusbar.showMessage(file)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainFrom()
    win.show()
    sys.exit(app.exec_())