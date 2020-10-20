# -*- coding: utf-8 -*-

"""
@File    : QuiApplication.py
@Time    : 2020/10/19 20:34
@Author  : sun
@Email   : 763224955@qq.com
@Software: PyCharm
"""

import sys
from PyQt5.QtWidgets import QHBoxLayout,QMainWindow,QApplication,QWidget,QPushButton

class QuitApplition(QMainWindow):
    def __init__(self):
        super(QuitApplition,self).__init__()
        self.resize(300,120)
        self.setWindowTitle('退出应用程序')

        # 添加button
        self.button1 = QPushButton("退出应用程序")
        # 不加lambda报错,具体原因无解
        # self.button1.clicked.connect(self.onClick_Button())
        self.button1.clicked.connect(lambda:self.onClick_Button())

        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)

    # 按钮单击事件的方法
    def onClick_Button(self):
        sender = self.sender()
        print(sender.text()+'按钮被按下')
        app =QApplication.instance()
        # 退出应用程序
        app.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QuitApplition()
    main.show()
    sys.exit(app.exec_())