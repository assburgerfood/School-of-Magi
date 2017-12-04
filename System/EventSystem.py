import glob
import json
import os
import random

from qtpy import QtGui


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
        self.__weight_sum = 0
        self.__scarcity = scarcity

        self.__events = EventDataReader(location).get_entity_data()
        self.generate_weights()

    def generate_weights(self):
        for event_name, event in self.__events.items():
            if event['probability'] != 0:
                self.__weight_list.setdefault(event['location'], {})
                self.__weight_list[event['location']].setdefault('sum', 0)
                self.__weight_list[event['location']]['sum'] += event['probability']
                self.__weight_list[event['location']].setdefault('event_weight', []).append(
                    (event_name, event['probability']))

    def get_event(self, event):
        return self.__events[event]

    def get_random_event(self, location):
        local_sum = self.__weight_list[location]['sum']
        r = random.randrange(self.__scarcity * local_sum)
        total_int = 0
        for event_weight in self.__weight_list[location]['event_weight']:
            total_int += event_weight[1]
            if total_int > r:
                return event_weight[0]
        return None

    # sets events picture from file
    def event_picture(self, scene):
        pic_location = self.event_data["scene" + str(scene)]["picture"]
        print("Picture file: ", pic_location)
        self.__picture = QtGui.QPixmap(pic_location)


class EventHandler:
    __current_event = None

    def __init__(self, event_data):
        self.event_data = event_data

        self.__scene_i = 1
        self.__text_i = 0

        self.__scenes = 0
        self.__scene = ''

    def set_random_event(self, location):
        try:
            event_name = self.event_data.get_random_event(location)
        except KeyError:
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

    def get_event_image(self):
        try:
            if 'tags' in self.__current_event[self.__scene]:
                return [self.__current_event[self.__scene]['tags'], self.__current_event[self.__scene]['pages']]
            else:
                return [self.__current_event[self.__scene]['picture']]
        except KeyError:
            return None

    def advance_event(self):
        if len(self.__current_event[self.__scene]['text']) < self.__text_i:
            self.__text_i += 1
            return True
        elif self.__scenes <= self.__scene_i:
            self.__text_i = 0
            self.__scene_i += 1
            self.__scene = 'scene{0}'.format(self.__scene_i)
            return True
        else:
            return False

    def advance_text(self):
        print("advancing text")
        if self.__text_i < len(self.__current_event[self.__scene]['text']) - 1:
            print("advancing text2")
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


def main():
    event_handler = EventHandler(EventLoader('Events'))
    if event_handler.set_random_event("School of Magi"):
        print(event_handler.get_event_text())
        print(event_handler.get_event_image())
        if event_handler.advance_text():
            print(event_handler.get_event_text())
            print(event_handler.get_event_image())


if __name__ == '__main__':
    main()
