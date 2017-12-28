import argparse

from System import CharBase
from System.EntityManager import LocationManager
from System.EventSystem import EventLoader, EventHandler
from System.ProgressData import ProgressData
from System.Time import Time


class MyGame:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    game_time = None
    progress_data = None

    getter = subparsers.add_parser('get')
    getters = ['stats', 'base', 'name', 'sex', 'location', 'location_list', 'new_event',
               'event_image', 'event_text', 'text_advancement', 'scene_advancement',
               'location_image', 'event_option', 'event_location', 'time', 'event_id']

    setters = ['location', 'event_scene']
    setter = subparsers.add_parser('set')

    savers = ['completed_event']
    saver = subparsers.add_parser('save')

    set_stats_parser = subparsers.add_parser('set stats')

    def __init__(self):
        self.player = CharBase.Hero()
        self.location_data = LocationManager()

        event_data = EventLoader()
        self.event_handler = EventHandler(event_data)

    def setup(self):
        print("choose new game, continue or exit")
        self.game_time = Time()

        self.set_stats_parser.add_argument('name', help="sets initial name", default="Daemon")
        self.set_stats_parser.add_argument('sex', help="sets initial sex")

        self.set_stats_parser.add_argument('health', type=int, help="sets initial health")
        self.set_stats_parser.add_argument('mana', type=int, help="sets initial mana")
        self.set_stats_parser.add_argument('stamina', type=int, help="sets initial stamina")
        self.set_stats_parser.add_argument('strength', type=int, help="sets initial strength")
        self.set_stats_parser.add_argument('magic', type=int, help="sets initial magic")
        self.set_stats_parser.add_argument('age', type=int, help="sets initial age")
        self.set_stats_parser.add_argument('gold', type=int, help="sets initial gold")

        self.getter.add_argument('type', choices=self.getters)
        self.setter.add_argument('type', choices=self.setters)
        self.saver.add_argument('type', choices=self.savers)

        self.setter.add_argument('data', help="data depending on the type", default=None)
        self.saver.add_argument('data', default=None)

        self.set_stats_parser.set_defaults(func=self.new_game)

        self.getter.set_defaults(func=self.get_data)
        self.setter.set_defaults(func=self.set_data)
        self.saver.set_defaults(func=self.save_data)

    def new_game(self, new_stats):
        print('new game started')
        self.player.new_base(new_stats["health"], new_stats["mana"], new_stats["stamina"],
                             new_stats["strength"], new_stats["magic"], new_stats["gold"],
                             new_stats["sex"], new_stats["name"], new_stats["age"])
        self.refill_hero_stats()

        # first time setup for progress saving
        self.progress_data_setup()

    def progress_data_setup(self):
        self.progress_data = ProgressData()
        self.progress_data.save_data_array('completed_events')

    # ------periodical event methods------
    def refill_hero_stats(self):
        self.player.refill_stats()

    # --------DATA SAVING-----------
    def save_data(self, data_type, data):
        switcher = {
            'completed_event': lambda: self.save_completed_event(data)
        }
        func = switcher.get(data_type, lambda: "nothing")
        func()

    def save_completed_event(self, event):
        self.progress_data.save_data_array('completed_events', event)

    # --------SETTERS-----------
    def set_data(self, data_type, data):
        switcher = {
            'location': lambda: self.set_location(data),
            'event_scene': lambda: self.set_event_scene(data)
        }
        func = switcher.get(data_type, lambda: "nothing")
        func()

    def set_location(self, location):
        print("active location set to: ", location)
        self.location_data.set_active_location(location)

    def set_event_scene(self, scene):
        self.event_handler.set_scene(scene)

    # time setters
    def advance_time(self, hour, minute):
        self.game_time.advance(hour, minute)

    # --------GETTERS-----------
    def get_data(self, data_type):
        switcher = {
            'stats': lambda: self.get_hero_stats(),
            'base': lambda: self.get_hero_base(),
            'name': lambda: self.get_hero_name(),
            'sex': lambda: self.get_hero_sex(),
            'time': lambda: self.get_time(),
            # location
            'location': lambda: self.get_hero_location(),
            'location_list': lambda: self.get_location_list(),
            'location_image': lambda: self.get_location_image(),
            # event
            'new_event': lambda: self.get_random_event(),
            'event_image': lambda: self.get_event_image(),
            'event_text': lambda: self.get_event_text(),
            'text_advancement': lambda: self.get_text_advancement(),
            'scene_advancement': lambda: self.get_scene_advancement(),
            'event_option': lambda: self.get_event_option(),
            'event_location': lambda: self.get_event_new_location(),
            'event_id': lambda: self.get_event_id()
        }
        func = switcher.get(data_type, lambda: "nothing")
        return func()

    def get_hero_stats(self):
        print("player stats: ", self.player.stats)
        return self.player.get_stats_dict()

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

    def get_location_image(self):
        return "System/Pictures/" + self.location_data.get_image(self.get_hero_location())

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
        completed_events_array = self.progress_data.get_data_array('completed_events')
        hero_stats_dict = self.get_hero_stats()
        return self.event_handler.set_random_event(self.get_hero_location(), int(self.get_hour()),
                                                   completed_events=completed_events_array,
                                                   stats_dict=hero_stats_dict)

    def get_event_option(self):
        return self.event_handler.get_event_option()

    def get_event_new_location(self):
        return self.event_handler.get_new_location()

    def get_event_id(self):
        return self.event_handler.get_event_name()

    # time getters
    def get_time(self):
        return self.game_time.get_time()

    def get_hour(self):
        return self.game_time.get_hour()
