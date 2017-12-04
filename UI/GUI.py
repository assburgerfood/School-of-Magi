from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QWidget
from qtpy import QtCore, QtWidgets, QtGui

from System import booruAPI
from UI import basewindow, newgame, creation, gamewidget


class MainWindow(QMainWindow, basewindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUI(self)

    # ------widget maintenance--------
    def add_widget(self, new_widget):
        self.centralwidget.addWidget(new_widget)

    def get_widget(self):
        return self.centralwidget.currentWidget()

    def set_widget(self, widget):
        self.centralwidget.setCurrentWidget(widget)


class NewGameWidget(QWidget, newgame.Ui_new_game_form):
    image = None
    resize_signal = pyqtSignal()
    lambda_array = []

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.change_pixmap("ass", 30)
        self.resize_signal.connect(lambda: self.resize_pixmap())  # Resize backgorund image

        self.btn_continue.clicked.connect(lambda: self.change_pixmap("anal", 20))

    def new_game_button(self, func):
        self.btn_new_game.clicked.connect(func)

    def change_pixmap(self, tags, pages):
        print("Picture changed")
        data = self.image_from_booru(tags, pages)
        locale_image = QImage()
        locale_image.loadFromData(data)
        self.image = QPixmap(locale_image)
        self.background_image.setPixmap(self.image.scaled(self.size(), aspectRatioMode=1))

    def image_from_booru(self, tags, pages):
        return booruAPI.YanGET(tags, pages).picture()

    def resizeEvent(self, event):
        self.resize_signal.emit()
        return super().resizeEvent(event)

    def resize_pixmap(self):
        self.background_image.setPixmap(self.image.scaled(self.size(), aspectRatioMode=1))


class CharacterCreationWidget(QWidget, creation.Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def create_character_button(self, func):
        self.btn_character.clicked.connect(func)

    def return_character_data(self):
        name = self.name_edit.text()
        sex = self.sex_value()
        health = self.value_health.text()
        mana = self.value_mana.text()
        stamina = self.value_stamina.text()
        strength = self.value_strength.text()
        magic = self.value_magic.text()
        age = str(self.age_spinner.value())
        return [name, sex, health, mana, stamina, strength, magic, age]

    def sex_value(self):
        if self.rbtn_female.isChecked():
            return "Female"
        elif self.rbtn_futanari.isChecked():
            return "Futanari"


# ---------MAIN GAME WIDGET-------------------------
class GameWindow(QWidget, gamewidget.Ui_main_game):
    image = None
    resize_signal = pyqtSignal()
    left_click = pyqtSignal()
    right_click = pyqtSignal()
    click_count = 0

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.set_web_image("anal", 20)
        self.resize_image_area()

        self.resize_signal.connect(lambda: self.resize_image_area())
        self.right_click.connect(lambda: self.text_on_off())
        self.left_click.connect(lambda: self.update_text())

    def raise_click_count(self):
        self.click_count += 1
        print("Clicks: ", self.click_count)

    def add_widget(self, widget):
        self.main_widget.addWidget(widget)

    @staticmethod
    def image_from_booru(tags, pages):
        return booruAPI.YanGET(tags, pages).picture()

    # ----------GUI updaters---------
    def refresh_stats(self, health, mana, stamina, max_health, max_mana, max_stamina, refresh_max=True):
        if refresh_max:
            self.bar_health.setMaximum(max_health)
            self.bar_mana.setMaximum(max_mana)
            self.bar_stamina.setMaximum(max_stamina)

        self.bar_health.setValue(health)
        self.bar_mana.setValue(mana)
        self.bar_stamina.setValue(stamina)

    def refresh_gold(self, gold):
        self.label_money.setText(str(gold) + " G")

    def resize_image(self):
        self.main_image.setPixmap(self.image.scaled(self.main_widget.size(), aspectRatioMode=1))

    def update_event(self, image_location, text):
        self.set_image(image_location)
        self.text_browser.setText(text)

    # -----------setters-------------
    def set_hero_name(self, name):
        self.label_name.setText(name)

    def set_text(self, text):
        self.text_browser.setText(text)

    def set_image(self, image_location):
        self.image = QtGui.QPixmap(image_location)
        self.resize_image()

    def set_web_image(self, tags, pages):
        data = self.image_from_booru(tags, pages)
        locale_image = QImage()
        locale_image.loadFromData(data)
        self.image = QPixmap(locale_image)
        self.resize_image()

    def set_location(self, location, location_array):
        self.current_location.setText(location)
        self.location_list.clear()
        self.set_location_list(location_array)

    def set_location_list(self, location_array):
        i = 0
        for location in location_array:
            item = QtWidgets.QListWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(14)
            item.setFont(font)
            self.location_list.addItem(item)

            item = self.location_list.item(i)
            item.setText(location)
            i += 1

    # -----------events--------------

    def resizeEvent(self, event):
        self.resize_signal.emit()
        return super().resizeEvent(event)

    def mousePressEvent(self, event):
        in_image_area = event.pos().x() > self.character_frame.width() \
                        and event.pos().y() > self.upper_frame.height()
        is_left_click = event.button() == 1
        is_right_click = event.button() == 2
        if in_image_area and is_left_click:
            self.left_click.emit()
        if in_image_area and is_right_click:
            self.right_click.emit()
        return super().mousePressEvent(event)

    # -----------lambda events-----------

    def resize_image_area(self):
        width = self.main_widget.width()
        height = self.main_widget.height()
        textbox_height = 200
        self.main_image.setGeometry(QtCore.QRect(0, 0, width, height))
        self.text_browser.setGeometry(QtCore.QRect(0, (height - textbox_height), width, textbox_height))
        self.resize_image()

    def text_on_off(self):
        if self.text_browser.isHidden():
            self.text_browser.show()
        else:
            self.text_browser.hide()

    def update_text(self):
        self.raise_click_count()
