from PyQt5.QtWidgets import QApplication

from System import GameCore
from UI.GUI import MainWindow, NewGameWidget, CharacterCreationWidget, GameWindow, OptionsWidget


class GameGUI:
    def __init__(self, game):
        # so you can give all your UI elements a game to play with
        self.game = game
        self.app = QApplication(sys.argv)
        self.new_game_window = MainWindow()  # GUI base window

        # -----widget creation----------
        self.startup_widget = NewGameWidget()  # startup widget
        self.creation_widget = CharacterCreationWidget()  # character creation widget
        self.main_game_widget = GameWindow()  # main game widget
        self.options_widget = None

        # start and populate the Ui_Game stuff
        self.widget_setup()

        # -----event connection creation------
        self.startup_event_connections()

        # add new game widget

    # -------set widgets---------
    def show_character_creation(self):
        self.new_game_window.set_widget(self.creation_widget)

    def show_main_game(self):
        self.new_game_window.set_widget(self.main_game_widget)
        # --------main game event connections--------
        self.create_location_menu_connection()

    def widget_setup(self):
        # adding widgets to game base
        self.new_game_window.add_widget(self.startup_widget)
        self.new_game_window.add_widget(self.creation_widget)
        self.new_game_window.add_widget(self.main_game_widget)
        # setting widget
        self.new_game_window.set_widget(self.startup_widget)

    # ------event connections--------
    def startup_event_connections(self):
        self.startup_widget.new_game_button(lambda: self.new_game_clicked())

    def create_character_connection(self):
        self.creation_widget.create_character_button(lambda: self.create_character_clicked())

    def create_location_menu_connection(self):
        self.main_game_widget.location_list.itemClicked.connect(lambda: self.location_clicked())

    def create_option_list_connection(self):
        self.options_widget.option_list.itemClicked.connect(lambda: self.option_clicked())

    def create_event_clicker_connection(self):
        self.main_game_widget.left_click.connect(lambda: self.event_clicked())

    def remove_left_click_connection(self):
        self.main_game_widget.left_click.disconnect()

    # ------events----------------
    def new_game_clicked(self):
        self.show_character_creation()
        self.create_character_connection()

    def create_character_clicked(self):
        self.show_main_game()
        new_parse_array = []
        new_stats = self.creation_widget.return_character_data()
        initial_gold = "100"

        new_parse_array.append("set stats")
        new_parse_array.extend(new_stats)
        new_parse_array.append(initial_gold)

        args = self.game.parser.parse_args(new_parse_array)
        args.func(vars(args))

        self.refresh_ui()  # stats refresh
        self.main_game_widget.set_hero_name(self.parse_getter("name"))  # setting hero name
        self.change_location()  # changing location

    def location_clicked(self):
        location = self.main_game_widget.location_list.currentItem().text()
        self.parse_setter("location", location)
        self.change_location()
        # event management
        if self.parse_getter("new_event"):  # check if new random event is available
            print("\nSTARTING RANDOM EVENT")
            self.main_game_widget.location_list.clear()
            self.update_event_in_gui()
            self.create_event_clicker_connection()

    def option_clicked(self):
        choice = self.options_widget.option_list.currentItem().text()
        option = self.parse_getter("event_option")[1]
        scene = [o for o in option if choice == o[0]][0][1]
        self.parse_setter("event_scene", scene)
        if scene != "end":
            location = self.parse_getter("event_location")
            if location:
                self.parse_setter("location", location)
            self.update_event_in_gui()
        else:
            self.change_location()
            self.remove_left_click_connection()
        self.options_widget.remove()

    def event_clicked(self):
        if self.parse_getter("text_advancement"):
            self.set_event_text()
        else:
            option = self.parse_getter("event_option")
            if option:
                self.options_widget = OptionsWidget()
                self.options_widget.setup(option[0], option[1])
                self.create_option_list_connection()
            elif self.parse_getter("scene_advancement"):
                self.update_event_in_gui()
            else:
                event_id = self.parse_getter('event_id')
                print(event_id)
                self.parse_saver('completed_event', event_id)
                self.remove_left_click_connection()
                self.change_location()

    # -------GUI modifiers----------

    def refresh_ui(self):
        stats = self.parse_getter("stats")
        base = self.parse_getter("base")
        time = self.parse_getter("time")

        self.main_game_widget.refresh_stats(stats['health'], stats['mana'], stats['stamina'],
                                            base['health'], base['mana'], base['stamina'])
        self.main_game_widget.refresh_gold(stats['gold'])
        self.main_game_widget.refresh_time(time)

    def change_location(self):
        print("\nCHANGING LOCATION")
        location = self.parse_getter("location")
        print("location get: ", location)
        location_array = self.parse_getter("location_list")
        print("array: ", location_array)
        location_image = self.parse_getter("location_image")
        print("image: ", location_image)
        self.main_game_widget.set_location(location, location_array, location_image)

    def set_text(self, text):
        self.main_game_widget.set_text(text)

    def set_image(self, data):
        if len(data) == 1:
            self.main_game_widget.set_image(data[0])
        else:
            self.main_game_widget.set_web_image(data[0], data[1])

    # -------parsers-------------
    def parse_getter(self, argument):
        args = self.game.parser.parse_args(["get", argument])
        return args.func(argument)

    def parse_setter(self, data_type, data=None):
        args = self.game.parser.parse_args(["set", data_type, data])
        args.func(data_type, data)

    def parse_saver(self, data_type, data=None):
        args = self.game.parser.parse_args(["save", data_type, data])
        args.func(data_type, data)

    # -------event management----
    def update_event_in_gui(self):
        self.set_event_image()
        self.set_event_text()

    def set_event_text(self):
        self.set_text(self.parse_getter("event_text"))

    def set_event_image(self):
        self.set_image(self.parse_getter("event_image"))

    # ------main loop-----------
    def main_loop(self):
        # wait for the UI to cease
        self.new_game_window.show()

        return self.app.exec_()


def start():
    # here you can argparse your CLI arguments, so you can choose
    # your interface (readline, ncurses, Qt, web, whatever...?)
    # and setup your application (logfile, port to bind to, look
    # of the GUI...)
    game = GameCore.MyGame()
    game.setup()

    return GameGUI(game).main_loop()


import sys

if __name__ == "__main__":
    sys.exit(start())
