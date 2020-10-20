# -*- coding: utf-8 -*-

"""
@File    : QuiApplication.py
@Time    : 2020/10/19 20:34
@Author  : sun
@Email   : 763224955@qq.com
@Software: PyCharm
"""

import sys
from PyQt5.QtWidgets import QHBoxLayout,QMainWindow,QApplication,QWidget,QPushButton,QToolTip
from PyQt5.QtGui import QFont

class TooltipForm_ex(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # QToolTip.setFont(QFont('SanSerif,12'))
        self.setToolTip('今天是个好天气<b>哈哈哈哈</b>')
        print('今天是个好天气<b>哈哈哈哈</b>')
        self.setGeometry(300,300,200,300)
        self.setWindowTitle("设置控件提示消息")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TooltipForm_ex()
    main.show()
    sys.exit(app.exec_())