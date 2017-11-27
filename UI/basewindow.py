# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'basewindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUI(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(1280, 720)

        self.centralwidget = QtWidgets.QStackedWidget(main_window)
        self.centralwidget.setMinimumSize(QtCore.QSize(640, 480))
        self.centralwidget.setObjectName("centralwidget")

        main_window.setCentralWidget(self.centralwidget)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "MainWindow"))
