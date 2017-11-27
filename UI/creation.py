# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'creation.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(860, 644)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.avatar_frame = QtWidgets.QFrame(Form)
        self.avatar_frame.setMinimumSize(QtCore.QSize(250, 0))
        self.avatar_frame.setObjectName("avatar_frame")

        self.image_layout = QtWidgets.QVBoxLayout(self.avatar_frame)
        self.image_layout.setObjectName("image_layout")

        self.character_image = QtWidgets.QLabel(self.avatar_frame)
        self.character_image.setAlignment(QtCore.Qt.AlignCenter)
        self.character_image.setObjectName("character_image")
        self.image_layout.addWidget(self.character_image)

        self.btn_character = QtWidgets.QPushButton(self.avatar_frame)
        self.btn_character.setObjectName("btn_character")
        self.image_layout.addWidget(self.btn_character, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_3.addWidget(self.avatar_frame)
        self.profile_frame = QtWidgets.QVBoxLayout()
        self.profile_frame.setObjectName("profile_frame")

        self.name_form = QtWidgets.QFormLayout()
        self.name_form.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldsStayAtSizeHint)
        self.name_form.setFormAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.name_form.setContentsMargins(-1, 5, -1, 5)
        self.name_form.setHorizontalSpacing(10)
        self.name_form.setObjectName("name_form")
        self.name_label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.name_form.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.name_label)
        self.name_edit = QtWidgets.QLineEdit(Form)
        self.name_edit.setObjectName("name_edit")
        self.name_form.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name_edit)
        self.profile_frame.addLayout(self.name_form)
        self.profile_tabs = QtWidgets.QTabWidget(Form)
        self.profile_tabs.setObjectName("profile_tabs")
        self.profile_tab = QtWidgets.QWidget()
        self.profile_tab.setObjectName("profile_tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.profile_tab)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.sex_box = QtWidgets.QGroupBox(self.profile_tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.sex_box.setFont(font)
        self.sex_box.setObjectName("sex_box")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.sex_box)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rbtn_futanari = QtWidgets.QRadioButton(self.sex_box)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        self.rbtn_futanari.setFont(font)
        self.rbtn_futanari.setObjectName("rbtn_futanari")
        self.horizontalLayout.addWidget(self.rbtn_futanari)
        self.rbtn_female = QtWidgets.QRadioButton(self.sex_box)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        self.rbtn_female.setFont(font)
        self.rbtn_female.setObjectName("rbtn_female")
        self.horizontalLayout.addWidget(self.rbtn_female)
        self.rbtn_female.setChecked(True)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self.sex_box)
        self.age_box = QtWidgets.QGroupBox(self.profile_tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.age_box.setFont(font)
        self.age_box.setObjectName("age_box")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.age_box)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.age_spinner = QtWidgets.QSpinBox(self.age_box)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.age_spinner.setFont(font)
        self.age_spinner.setMinimum(14)
        self.age_spinner.setMaximum(19)
        self.age_spinner.setObjectName("age_spinner")
        self.horizontalLayout_2.addWidget(self.age_spinner)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.age_box)
        self.stats_box = QtWidgets.QGroupBox(self.profile_tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.stats_box.setFont(font)
        self.stats_box.setObjectName("stats_box")
        self.gridLayout = QtWidgets.QGridLayout(self.stats_box)
        self.gridLayout.setObjectName("gridLayout")
        self.value_stamina = QtWidgets.QLabel(self.stats_box)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        self.value_stamina.setFont(font)
        self.value_stamina.setObjectName("value_stamina")
        self.gridLayout.addWidget(self.value_stamina, 0, 2, 1, 1)
        self.slider_stamina = QtWidgets.QSlider(self.stats_box)
        self.slider_stamina.setMinimum(10)
        self.slider_stamina.setMaximum(15)
        self.slider_stamina.setOrientation(QtCore.Qt.Horizontal)
        self.slider_stamina.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.slider_stamina.setTickInterval(1)
        self.slider_stamina.setObjectName("slider_stamina")
        self.gridLayout.addWidget(self.slider_stamina, 0, 1, 1, 1)
        self.label_stamina = QtWidgets.QLabel(self.stats_box)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        self.label_stamina.setFont(font)
        self.label_stamina.setObjectName("label_stamina")
        self.gridLayout.addWidget(self.label_stamina, 0, 0, 1, 1)
        self.value_health = QtWidgets.QLabel(self.stats_box)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        self.value_health.setFont(font)
        self.value_health.setObjectName("value_health")
        self.gridLayout.addWidget(self.value_health, 1, 2, 1, 1)
        self.value_mana = QtWidgets.QLabel(self.stats_box)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        self.value_mana.setFont(font)
        self.value_mana.setObjectName("value_mana")
        self.gridLayout.addWidget(self.value_mana, 2, 2, 1, 1)
        self.label_health = QtWidgets.QLabel(self.stats_box)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        self.label_health.setFont(font)
        self.label_health.setObjectName("label_health")
        self.gridLayout.addWidget(self.label_health, 1, 0, 1, 1)
        self.slider_health = QtWidgets.QSlider(self.stats_box)
        self.slider_health.setMinimum(5)
        self.slider_health.setMaximum(15)
        self.slider_health.setOrientation(QtCore.Qt.Horizontal)
        self.slider_health.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.slider_health.setTickInterval(1)
        self.slider_health.setObjectName("slider_health")
        self.gridLayout.addWidget(self.slider_health, 1, 1, 1, 1)
        self.label_mana = QtWidgets.QLabel(self.stats_box)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        self.label_mana.setFont(font)
        self.label_mana.setObjectName("label_mana")
        self.gridLayout.addWidget(self.label_mana, 2, 0, 1, 1)
        self.label_stength = QtWidgets.QLabel(self.stats_box)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        self.label_stength.setFont(font)
        self.label_stength.setObjectName("label_stength")
        self.gridLayout.addWidget(self.label_stength, 3, 0, 1, 1)
        self.value_magic = QtWidgets.QLabel(self.stats_box)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        self.value_magic.setFont(font)
        self.value_magic.setObjectName("value_magic")
        self.gridLayout.addWidget(self.value_magic, 4, 2, 1, 1)
        self.slider_strength = QtWidgets.QSlider(self.stats_box)
        self.slider_strength.setMinimum(5)
        self.slider_strength.setMaximum(15)
        self.slider_strength.setOrientation(QtCore.Qt.Horizontal)
        self.slider_strength.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.slider_strength.setTickInterval(1)
        self.slider_strength.setObjectName("slider_strength")
        self.gridLayout.addWidget(self.slider_strength, 3, 1, 1, 1)
        self.slider_mana = QtWidgets.QSlider(self.stats_box)
        self.slider_mana.setMinimum(5)
        self.slider_mana.setMaximum(15)
        self.slider_mana.setOrientation(QtCore.Qt.Horizontal)
        self.slider_mana.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.slider_mana.setTickInterval(1)
        self.slider_mana.setObjectName("slider_mana")
        self.gridLayout.addWidget(self.slider_mana, 2, 1, 1, 1)
        self.value_strength = QtWidgets.QLabel(self.stats_box)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        self.value_strength.setFont(font)
        self.value_strength.setObjectName("value_strength")
        self.gridLayout.addWidget(self.value_strength, 3, 2, 1, 1)
        self.labe_magic = QtWidgets.QLabel(self.stats_box)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        self.labe_magic.setFont(font)
        self.labe_magic.setObjectName("labe_magic")
        self.gridLayout.addWidget(self.labe_magic, 4, 0, 1, 1)
        self.slider_magic = QtWidgets.QSlider(self.stats_box)
        self.slider_magic.setMinimum(5)
        self.slider_magic.setMaximum(15)
        self.slider_magic.setOrientation(QtCore.Qt.Horizontal)
        self.slider_magic.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.slider_magic.setTickInterval(1)
        self.slider_magic.setObjectName("slider_magic")
        self.gridLayout.addWidget(self.slider_magic, 4, 1, 1, 1)
        self.verticalLayout.addWidget(self.stats_box)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.profile_tabs.addTab(self.profile_tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.profile_tabs.addTab(self.tab_2, "")
        self.profile_frame.addWidget(self.profile_tabs)
        self.horizontalLayout_3.addLayout(self.profile_frame)
        self.name_label.setBuddy(self.name_edit)

        self.retranslateUi(Form)
        self.profile_tabs.setCurrentIndex(0)
        self.slider_stamina.valueChanged['int'].connect(self.value_stamina.setNum)
        self.slider_health.valueChanged['int'].connect(self.value_health.setNum)
        self.slider_mana.valueChanged['int'].connect(self.value_mana.setNum)
        self.slider_strength.valueChanged['int'].connect(self.value_strength.setNum)
        self.slider_magic.valueChanged['int'].connect(self.value_magic.setNum)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.character_image.setText(_translate("Form", "No Image"))
        self.btn_character.setText(_translate("Form", "Create Character"))
        self.name_label.setText(_translate("Form", "Name"))
        self.sex_box.setTitle(_translate("Form", "Sex"))
        self.rbtn_futanari.setText(_translate("Form", "Futanari"))
        self.rbtn_female.setText(_translate("Form", "Female"))
        self.age_box.setTitle(_translate("Form", "Age"))
        self.stats_box.setTitle(_translate("Form", "Stats"))
        self.value_stamina.setText(_translate("Form", "10"))
        self.label_stamina.setText(_translate("Form", "Stamina"))
        self.value_health.setText(_translate("Form", "5"))
        self.value_mana.setText(_translate("Form", "5"))
        self.label_health.setText(_translate("Form", "Health"))
        self.label_mana.setText(_translate("Form", "Mana"))
        self.label_stength.setText(_translate("Form", "Strength"))
        self.value_magic.setText(_translate("Form", "5"))
        self.value_strength.setText(_translate("Form", "5"))
        self.labe_magic.setText(_translate("Form", "Magic"))
        self.profile_tabs.setTabText(self.profile_tabs.indexOf(self.profile_tab), _translate("Form", "Profile"))
        self.profile_tabs.setTabText(self.profile_tabs.indexOf(self.tab_2), _translate("Form", "Tab 2"))