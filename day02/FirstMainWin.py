# -*- coding: utf-8 -*-

"""
@File    : FirstMainWin.py
@Time    : 2020/10/15 23:03
@Author  : sun
@Email   : 763224955@qq.com
@Software: PyCharm
"""

import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon

class FirstMainWin(QMainWindow):
    def __init__(self,parent=None):
        super(FirstMainWin,self).__init__(parent)