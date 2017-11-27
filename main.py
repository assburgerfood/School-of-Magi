from PyQt5.QtWidgets import QApplication

from System import GameCore
from UI.GUI import MainWindow, NewGameWidget, CharacterCreationWidget, GameWindow


class GameGUI:
    def __init__(self, game):
        # so you can give all your UI elements a game to play with
        self.game = game
        self.app = QApplication(sys.argv)

        self.new_game_window = MainWindow()  # GUI base window

        self.startup_widget = NewGameWidget()  # startup widget
        self.creation_widget = CharacterCreationWidget()  # character creation widget
        self.main_game_widget = GameWindow()  # main game widget

        # start and populate the Ui_Game stuff
        self.startup_widgets()
        self.startup_event_connections()


        # add new game widget

    # -------set widgets---------
    def set_to_creation(self):
        self.new_game_window.set_widget(self.creation_widget)

    def set_to_main_game(self):
        self.new_game_window.set_widget(self.main_game_widget)

    def startup_widgets(self):
        self.new_game_window.add_widget(self.startup_widget)
        self.new_game_window.add_widget(self.creation_widget)
        self.new_game_window.add_widget(self.main_game_widget)

        self.new_game_window.set_widget(self.startup_widget)

    # ------event connections--------
    def startup_event_connections(self):
        self.startup_widget.new_game_button(lambda: self.new_game_clicked())

    def create_character_connection(self):
        self.creation_widget.create_character_button(lambda: self.create_character_clicked())

    # ------events----------------
    def new_game_clicked(self):
        self.set_to_creation()
        self.create_character_connection()

    def create_character_clicked(self):
        self.set_to_main_game()
        new_parse_array = []
        new_stats = self.creation_widget.return_character_data()
        initial_gold = "100"

        new_parse_array.append("set stats")
        new_parse_array.extend(new_stats)
        new_parse_array.append(initial_gold)

        args = self.game.parser.parse_args(new_parse_array)
        args.func(vars(args))

        self.refresh_ui()
        self.main_game_widget.set_hero_name(self.parse_getter("name"))

    # -------GUI modifiers----------
    def refresh_ui(self):
        stats = self.parse_getter("stats")
        base = self.parse_getter("base")

        self.main_game_widget.refresh_stats(stats['health'], stats['mana'], stats['stamina'],
                                            base['health'], base['mana'], base['stamina'])

        self.main_game_widget.refresh_gold(stats['gold'])

    # -------parsers-------------
    def parse_getter(self, argument):
        args = self.game.parser.parse_args(["get", argument])
        return args.func(argument)

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
