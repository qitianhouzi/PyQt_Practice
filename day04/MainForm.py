# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainForm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MianWindow(object):
    def setupUi(self, MianWindow):
        MianWindow.setObjectName("MianWindow")
        MianWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MianWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 210, 93, 28))
        self.pushButton.setObjectName("pushButton")
        MianWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MianWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MianWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MianWindow)
        self.statusbar.setObjectName("statusbar")
        MianWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MianWindow)
        self.toolBar.setObjectName("toolBar")
        MianWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        MianWindow.insertToolBarBreak(self.toolBar)
        self.fileOpenAction = QtWidgets.QAction(MianWindow)
        self.fileOpenAction.setObjectName("fileOpenAction")
        self.actionfileNewAction = QtWidgets.QAction(MianWindow)
        self.actionfileNewAction.setObjectName("actionfileNewAction")
        self.actionfileCloseFile = QtWidgets.QAction(MianWindow)
        self.actionfileCloseFile.setObjectName("actionfileCloseFile")
        self.addWinAction = QtWidgets.QAction(MianWindow)
        self.addWinAction.setObjectName("addWinAction")
        self.menu.addAction(self.fileOpenAction)
        self.menu.addAction(self.actionfileNewAction)
        self.menu.addAction(self.actionfileCloseFile)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.toolBar.addAction(self.addWinAction)

        self.retranslateUi(MianWindow)
        QtCore.QMetaObject.connectSlotsByName(MianWindow)

    def retranslateUi(self, MianWindow):
        _translate = QtCore.QCoreApplication.translate
        MianWindow.setWindowTitle(_translate("MianWindow", "MainWindow"))
        self.pushButton.setText(_translate("MianWindow", "打开"))
        self.menu.setTitle(_translate("MianWindow", "文件(&F)"))
        self.menu_2.setTitle(_translate("MianWindow", "编辑(&E)"))
        self.toolBar.setWindowTitle(_translate("MianWindow", "toolBar"))
        self.fileOpenAction.setText(_translate("MianWindow", "打开"))
        self.fileOpenAction.setShortcut(_translate("MianWindow", "Alt+O"))
        self.actionfileNewAction.setText(_translate("MianWindow", "新建"))
        self.actionfileNewAction.setShortcut(_translate("MianWindow", "Alt+N"))
        self.actionfileCloseFile.setText(_translate("MianWindow", "关闭"))
        self.actionfileCloseFile.setShortcut(_translate("MianWindow", "Alt+C"))
        self.addWinAction.setText(_translate("MianWindow", "添加窗体"))
        self.addWinAction.setToolTip(_translate("MianWindow", "添加窗体"))

