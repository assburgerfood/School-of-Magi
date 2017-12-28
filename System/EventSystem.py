import glob
import json
import os
import random
from pprint import pprint


class EventDataReader:
    __contents = {}

    def __init__(self, json_dir_name):
        json_pattern = os.path.join(json_dir_name, '*.json')
        file_list = glob.glob(json_pattern)
        for file in file_list:
            event_key = file[file.find('\\') + 1:file.find('.json')]
            with open(file) as data_file:
                self.__contents[event_key] = json.load(data_file)

    def get_entity_data(self):
        return self.__contents


class EventLoader:
    __text = ""
    __picture = None

    def __init__(self, location="System/Events", scarcity=2):

        self.__weight_list = {}
        self.__scarcity = scarcity

        self.__events = EventDataReader(location).get_entity_data()
        self.generate_weights()
        self.setup()
        # pprint(self.__events)
        # pprint(self.__weight_list)

    def setup(self):
        for event_name, event in self.__events.items():
            event['id'] = event_name

    def generate_weights(self):
        for event_name, event in self.__events.items():
            if event['probability'] != 0:
                self.__weight_list.setdefault(event['location'], {})
                if 'requirements' in event:
                    self.__weight_list[event['location']].setdefault('event_weight', []).append(
                        (event_name, event['probability'], event['requirements']))
                else:
                    self.__weight_list[event['location']].setdefault('event_weight', []).append(
                        (event_name, event['probability']))

    def get_sum(self, event_list):
        local_sum = 0
        local_event_list = event_list
        for event in local_event_list:
            local_sum += event[1]
        return local_sum

    def get_reduced_weight_events(self, location, hour, completed_events, stats_dict):
        new_event_list = []
        for event in self.__weight_list[location]['event_weight']:
            if len(event) == 2:
                new_event_list.append(event)
            else:
                req = event[2]
                if self.requirement_checker('time', req, hour) and \
                        self.requirement_checker('completed_events', req, completed_events) and not \
                        self.requirement_checker('!completed_events', req, completed_events) and \
                        self.requirement_checker('stats', req, stats_dict):
                    new_event_list.append((event[0], event[1]))
        return new_event_list

    def requirement_checker(self, value, requirements, comparison):
        if value not in requirements:
            return True
        switcher = {
            'completed_events': lambda: set(requirements[value]).issubset(set(comparison)),
            '!completed_events': lambda: set(requirements[value]).issubset(set(comparison)),
            'time': lambda: requirements[value][0] <= comparison <= requirements[value][1],
            'stats': lambda: self.dict_comparison(requirements[value], comparison)
        }
        func = switcher.get(value, lambda: "nothing")
        return func()

    def dict_comparison(self, required_stats, comparison):
        for key, value in required_stats.items():
            if value[0] == '>':
                if comparison[key] < int(value[1:]):
                    return False
                else:
                    return True
            elif value[0] == '<':
                if comparison[key] > int(value[1:]):
                    return False
                else:
                    return True
            else:
                print("Error in 'dict_comparison'")
                return False

    def get_event(self, event):
        return self.__events[event]

    def get_random_event(self, location, hour=13, completed_events=None, stats_dict=None):
        if stats_dict is None:
            stats_dict = {}
        if completed_events is None:
            completed_events = []
        local_event_list = self.get_reduced_weight_events(location, hour, completed_events, stats_dict)
        pprint(local_event_list)
        local_sum = self.get_sum(local_event_list)
        r = random.randrange(self.__scarcity * local_sum)
        total_int = 0
        for event in local_event_list:
            total_int += event[1]
            if total_int > r:
                return event[0]
        return None


class EventHandler:
    __current_event = None

    def __init__(self, event_data):
        self.event_data = event_data

        self.__scene_i = 1
        self.__text_i = 0

        self.__scenes = 0
        self.__scene = ''

    def clear_event(self):
        self.__current_event = None

        self.__scene_i = 1
        self.__text_i = 0

        self.__scenes = 0
        self.__scene = ''

    def set_random_event(self, location, hour, completed_events=None, stats_dict=None):
        try:
            event_name = self.event_data.get_random_event(location, hour, completed_events, stats_dict)
        except KeyError:
            print("KeyError in 'EventSystem.set_random_event()")
            return False
        if event_name:
            self.__current_event = self.event_data.get_event(event_name)
            self.__scene_i = 1
            self.__text_i = 0
            self.__scenes = len([key for key in self.__current_event.keys() if key.startswith('scene')])
            self.__scene = 'scene1'
            return True
        else:
            return False

    def get_event_text(self):
        try:
            return self.__current_event[self.__scene]['text'][self.__text_i]
        except IndexError:
            return None

    def get_new_location(self):
        try:
            if 'new_location' in self.__current_event[self.__scene]:
                return self.__current_event[self.__scene]['new_location']
            else:
                return None
        except KeyError:
            return None

    def get_event_image(self):
        try:
            if 'tags' in self.__current_event[self.__scene]:
                return [self.__current_event[self.__scene]['tags'],
                        self.__current_event[self.__scene]['pages']]
            else:
                return ['System/Pictures/' + self.__current_event[self.__scene]['picture']]
        except KeyError:
            return None

    def get_event_option(self):
        try:
            if 'option' in self.__current_event[self.__scene]:
                return self.__current_event[self.__scene]['option']['text'], \
                       self.__current_event[self.__scene]['option']['options']
            else:
                return None
        except KeyError:
            return None

    def set_scene(self, scene):
        if scene == 'end':
            self.clear_event()
        else:
            self.__text_i = 0
            self.__scene = scene
            self.__scene_i = int(scene[-1])

    def advance_text(self):
        if self.__text_i < len(self.__current_event[self.__scene]['text']) - 1:
            self.__text_i += 1
            return True
        else:
            return False

    def advance_scene(self):
        self.__text_i = 0
        if self.__scene_i < self.__scenes:
            self.__scene_i += 1
            self.__scene = 'scene{0}'.format(self.__scene_i)
            return True
        else:
            return False

    def get_event_name(self):
        return self.__current_event['id']


def main():
    event_handler = EventHandler(EventLoader('Events'))
    if event_handler.set_random_event("School of Magi", hour=13,
                                      completed_events=["school_mastur"],
                                      stats_dict={'health': 5, 'mana': 5, 'strength': 5, 'magic': 5, 'gold': 100,
                                                  'stamina': 10, 'age': 14}):
        print(event_handler.get_event_text())
        print(event_handler.get_event_image())
        if event_handler.advance_text():
            print(event_handler.get_event_text())
            print(event_handler.get_event_image())


if __name__ == '__main__':
    main()
