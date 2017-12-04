# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gamewidget.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_main_game(object):
    def setupUi(self, main_game):
        main_game.setObjectName("main_game")
        main_game.resize(1071, 786)
        main_game.setMinimumSize(QtCore.QSize(640, 480))
        self.verticalLayout = QtWidgets.QVBoxLayout(main_game)
        self.verticalLayout.setObjectName("verticalLayout")
        self.upper_frame = QtWidgets.QFrame(main_game)
        self.upper_frame.setMaximumSize(QtCore.QSize(16777215, 200))
        self.upper_frame.setObjectName("upper_frame")
        self.upper_box = QtWidgets.QHBoxLayout(self.upper_frame)
        self.upper_box.setObjectName("upper_box")
        self.location_layout = QtWidgets.QVBoxLayout()
        self.location_layout.setObjectName("location_layout")
        self.current_location = QtWidgets.QLabel(self.upper_frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.current_location.setFont(font)
        self.current_location.setObjectName("current_location")
        self.location_layout.addWidget(self.current_location)
        self.location_list = QtWidgets.QListWidget(self.upper_frame)
        self.location_list.setObjectName("location_list")
        self.location_layout.addWidget(self.location_list)
        self.upper_box.addLayout(self.location_layout)
        self.event_list = QtWidgets.QListWidget(self.upper_frame)
        self.event_list.setAlternatingRowColors(True)
        self.event_list.setObjectName("event_list")
        self.upper_box.addWidget(self.event_list)
        self.tab_widget = QtWidgets.QTabWidget(self.upper_frame)
        self.tab_widget.setObjectName("tab_widget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tab_widget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tab_widget.addTab(self.tab_2, "")
        self.upper_box.addWidget(self.tab_widget)
        self.verticalLayout.addWidget(self.upper_frame)
        self.lower_box = QtWidgets.QHBoxLayout()
        self.lower_box.setObjectName("lower_box")
        self.character_frame = QtWidgets.QFrame(main_game)
        self.character_frame.setMinimumSize(QtCore.QSize(0, 440))
        self.character_frame.setMaximumSize(QtCore.QSize(350, 16777215))
        self.character_frame.setObjectName("character_frame")
        self.char_box = QtWidgets.QVBoxLayout(self.character_frame)
        self.char_box.setObjectName("char_box")
        self.label_name = QtWidgets.QLabel(self.character_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_name.setFont(font)
        self.label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name.setObjectName("label_name")
        self.char_box.addWidget(self.label_name)
        self.label_money = QtWidgets.QLabel(self.character_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_money.setFont(font)
        self.label_money.setAlignment(QtCore.Qt.AlignCenter)
        self.label_money.setObjectName("label_money")
        self.char_box.addWidget(self.label_money)
        self.line_1 = QtWidgets.QFrame(self.character_frame)
        self.line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_1.setObjectName("line_1")
        self.char_box.addWidget(self.line_1)
        self.line_2 = QtWidgets.QFrame(self.character_frame)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.char_box.addWidget(self.line_2)
        self.stats_layout = QtWidgets.QFormLayout()
        self.stats_layout.setObjectName("stats_layout")
        self.label_health = QtWidgets.QLabel(self.character_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_health.setFont(font)
        self.label_health.setObjectName("label_health")
        self.stats_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_health)
        self.bar_health = QtWidgets.QProgressBar(self.character_frame)
        self.bar_health.setStyleSheet("background-color: yellow;\n"
"color: rgb(0, 0, 0);")
        self.bar_health.setProperty("value", 0)
        self.bar_health.setTextVisible(False)
        self.bar_health.setObjectName("bar_health")
        self.stats_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.bar_health)
        self.label_mana = QtWidgets.QLabel(self.character_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_mana.setFont(font)
        self.label_mana.setObjectName("label_mana")
        self.stats_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_mana)
        self.bar_mana = QtWidgets.QProgressBar(self.character_frame)
        self.bar_mana.setProperty("value", 0)
        self.bar_mana.setTextVisible(False)
        self.bar_mana.setObjectName("bar_mana")
        self.stats_layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.bar_mana)
        self.label_stamina = QtWidgets.QLabel(self.character_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_stamina.setFont(font)
        self.label_stamina.setObjectName("label_stamina")
        self.stats_layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_stamina)
        self.bar_stamina = QtWidgets.QProgressBar(self.character_frame)
        self.bar_stamina.setProperty("value", 0)
        self.bar_stamina.setTextVisible(False)
        self.bar_stamina.setObjectName("bar_stamina")
        self.stats_layout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.bar_stamina)
        self.char_box.addLayout(self.stats_layout)
        self.character_image = QtWidgets.QLabel(self.character_frame)
        self.character_image.setAlignment(QtCore.Qt.AlignCenter)
        self.character_image.setObjectName("character_image")
        self.char_box.addWidget(self.character_image)
        self.char_box.setStretch(0, 1)
        self.char_box.setStretch(1, 1)
        self.char_box.setStretch(5, 10)
        self.lower_box.addWidget(self.character_frame)
        self.main_widget = QtWidgets.QStackedWidget(main_game)
        self.main_widget.setMinimumSize(QtCore.QSize(480, 0))
        self.main_widget.setObjectName("main_widget")
        self.widget_1 = QtWidgets.QWidget()
        self.widget_1.setObjectName("widget_1")
        self.main_image = QtWidgets.QLabel(self.widget_1)
        self.main_image.setGeometry(QtCore.QRect(120, 80, 221, 161))
        self.main_image.setAlignment(QtCore.Qt.AlignCenter)
        self.main_image.setObjectName("main_image")
        self.text_browser = QtWidgets.QTextBrowser(self.widget_1)
        self.text_browser.setGeometry(QtCore.QRect(110, 240, 256, 192))
        self.text_browser.setStyleSheet("background-color: rgba(85, 170, 255,150);")
        self.text_browser.setSource(QtCore.QUrl("file:///D:/Jan/Programming/"))
        self.text_browser.setOpenLinks(False)
        self.text_browser.setObjectName("text_browser")
        self.main_widget.addWidget(self.widget_1)
        self.lower_box.addWidget(self.main_widget)
        self.lower_box.setStretch(0, 1)
        self.verticalLayout.addLayout(self.lower_box)

        self.retranslateUi(main_game)
        self.tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main_game)

    def retranslateUi(self, main_game):
        _translate = QtCore.QCoreApplication.translate
        main_game.setWindowTitle(_translate("main_game", "Form"))
        self.current_location.setText(_translate("main_game", "current_location"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab), _translate("main_game", "Tab 1"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_2), _translate("main_game", "Tab 2"))
        self.label_name.setText(_translate("main_game", "name"))
        self.label_money.setText(_translate("main_game", "gold"))
        self.label_health.setText(_translate("main_game", "Health"))
        self.bar_health.setFormat(_translate("main_game", "%v"))
        self.label_mana.setText(_translate("main_game", "Mana"))
        self.bar_mana.setFormat(_translate("main_game", "%v"))
        self.label_stamina.setText(_translate("main_game", "Stamina"))
        self.bar_stamina.setFormat(_translate("main_game", "%v"))
        self.character_image.setText(_translate("main_game", "no image"))
        self.main_image.setText(_translate("main_game", "main picture"))

