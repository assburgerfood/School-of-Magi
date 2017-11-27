# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newgame.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_new_game_form(object):
    def setupUi(self, new_game_form):
        new_game_form.setObjectName("new_game_form")
        new_game_form.resize(1280, 720)

        self.new_game_layout = QtWidgets.QVBoxLayout(new_game_form)
        self.new_game_layout.setObjectName("new_game_layout")

        self.background_image = QtWidgets.QLabel(new_game_form)
        self.background_image.setAlignment(QtCore.Qt.AlignCenter)
        self.background_image.setObjectName("background_image")

        self.new_game_layout.addWidget(self.background_image)

        self.horizontalWidget = QtWidgets.QWidget(new_game_form)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())

        self.horizontalWidget.setSizePolicy(sizePolicy)
        self.horizontalWidget.setObjectName("horizontalWidget")

        self.button_layout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.button_layout.setContentsMargins(0, 0, 0, 0)
        self.button_layout.setObjectName("button_layout")

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.button_layout.addItem(spacerItem)

        self.btn_new_game = QtWidgets.QPushButton(self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_new_game.sizePolicy().hasHeightForWidth())
        self.btn_new_game.setSizePolicy(sizePolicy)
        self.btn_new_game.setMinimumSize(QtCore.QSize(150, 0))
        self.btn_new_game.setObjectName("btn_new_game")
        self.button_layout.addWidget(self.btn_new_game)
        self.btn_continue = QtWidgets.QPushButton(self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_continue.sizePolicy().hasHeightForWidth())
        self.btn_continue.setSizePolicy(sizePolicy)
        self.btn_continue.setMinimumSize(QtCore.QSize(150, 0))
        self.btn_continue.setObjectName("btn_continue")
        self.button_layout.addWidget(self.btn_continue)
        self.btn_exit = QtWidgets.QPushButton(self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        self.btn_exit.setMinimumSize(QtCore.QSize(150, 0))
        self.btn_exit.setObjectName("btn_exit")
        self.button_layout.addWidget(self.btn_exit)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.button_layout.addItem(spacerItem1)

        self.new_game_layout.addWidget(self.horizontalWidget)

        self.retranslateUi(new_game_form)
        QtCore.QMetaObject.connectSlotsByName(new_game_form)

    def retranslateUi(self, new_game_form):
        _translate = QtCore.QCoreApplication.translate
        new_game_form.setWindowTitle(_translate("new_game_form", "Form"))
        self.background_image.setText(_translate("new_game_form", "No Image"))
        self.btn_new_game.setText(_translate("new_game_form", "New Game"))
        self.btn_continue.setText(_translate("new_game_form", "Continue"))
        self.btn_exit.setText(_translate("new_game_form", "Exit"))
