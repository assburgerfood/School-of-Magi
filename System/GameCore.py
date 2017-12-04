import argparse

from System import CharBase
from System.EntityManager import LocationManager
from System.EventSystem import EventLoader, EventHandler


class MyGame:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    set_stats_parser = subparsers.add_parser('set stats')
    getter = subparsers.add_parser('get')
    setter = subparsers.add_parser('set')

    def __init__(self):
        self.player = CharBase.Hero()
        self.location_data = LocationManager()

        event_data = EventLoader()
        self.event_handler = EventHandler(event_data)

    def setup(self):
        print("choose new game, continue or exit")

        self.set_stats_parser.add_argument('name', help="sets initial name", default="Daemon")
        self.set_stats_parser.add_argument('sex', help="sets initial sex")

        self.set_stats_parser.add_argument('health', type=int, help="sets initial health")
        self.set_stats_parser.add_argument('mana', type=int, help="sets initial mana")
        self.set_stats_parser.add_argument('stamina', type=int, help="sets initial stamina")
        self.set_stats_parser.add_argument('strength', type=int, help="sets initial strength")
        self.set_stats_parser.add_argument('magic', type=int, help="sets initial magic")
        self.set_stats_parser.add_argument('age', type=int, help="sets initial age")
        self.set_stats_parser.add_argument('gold', type=int, help="sets initial gold")

        self.getter.add_argument('type', choices=['stats', 'base', 'name', 'sex',
                                                  'location', 'location_list', 'new_event',
                                                  'event_image', 'event_text', 'text_advancement',
                                                  'scene_advancement'])

        self.setter.add_argument('type', choices=['location'])
        self.setter.add_argument('data', help="data depending on the type", default=None)

        self.set_stats_parser.set_defaults(func=self.new_game)
        self.getter.set_defaults(func=self.get_data)
        self.setter.set_defaults(func=self.set_data)

    def new_game(self, new_stats):
        print('new game started')
        self.player.new_base(new_stats["health"], new_stats["mana"], new_stats["stamina"],
                             new_stats["strength"], new_stats["magic"], new_stats["gold"],
                             new_stats["sex"], new_stats["name"], new_stats["age"])
        self.refill_hero_stats()

    # ------periodical event methods------
    def refill_hero_stats(self):
        self.player.refill_stats()

    # --------SETTERS-----------
    def set_data(self, data_type, data):
        switcher = {
            'location': lambda: self.set_location(data)
        }
        func = switcher.get(data_type, lambda: "nothing")
        func()

    def set_location(self, location):
        print("active location set to: ", location)
        self.location_data.set_active_location(location)

    # --------GETTERS-----------
    def get_data(self, data_type):
        switcher = {
            'stats': lambda: self.get_hero_stats(),
            'base': lambda: self.get_hero_base(),
            'name': lambda: self.get_hero_name(),
            'sex': lambda: self.get_hero_sex(),
            'location': lambda: self.get_hero_location(),
            'location_list': lambda: self.get_location_list(),
            'new_event': lambda: self.get_random_event(),
            'event_image': lambda: self.get_event_image(),
            'event_text': lambda: self.get_event_text(),
            'text_advancement': lambda: self.get_text_advancement(),
            'scene_advancement': lambda: self.get_scene_advancement()
        }
        func = switcher.get(data_type, lambda: "nothing")
        return func()

    def get_hero_stats(self):
        print("player stats: ", self.player.stats)
        return self.player.stats

    def get_hero_base(self):
        return self.player.base

    def get_hero_name(self):
        return self.player.name

    def get_hero_sex(self):
        return self.player.sex

    # location getters
    def get_hero_location(self):
        return self.location_data.get_active_location()

    def get_location_list(self):
        return self.location_data.get_nearby_locations(self.get_hero_location())

    # event getters
    def get_event_image(self):
        return self.event_handler.get_event_image()

    def get_event_text(self):
        return self.event_handler.get_event_text()

    def get_text_advancement(self):
        return self.event_handler.advance_text()

    def get_scene_advancement(self):
        return self.event_handler.advance_scene()

    def get_random_event(self):
        return self.event_handler.set_random_event(self.get_hero_location())
