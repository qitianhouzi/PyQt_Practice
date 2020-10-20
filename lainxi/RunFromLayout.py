# -*- coding: utf-8 -*-

"""
@File    : Run.py
@Time    : 2020/10/15 20:50
@Author  : sun
@Email   : 763224955@qq.com
@Software: PyCharm
"""
import sys
from lainxi import FronLayoutEX
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindows = QMainWindow()
    ui = FronLayoutEX.Ui_MainWindow()
    ui.setupUi(mainWindows)
    mainWindows.show()
    sys.exit(app.exec_())