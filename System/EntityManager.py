import glob
import json
import os
from pprint import pprint


class EntityDataReader:
    __contents = []

    def __init__(self, json_dir_name):
        json_pattern = os.path.join(json_dir_name, '*.json')
        file_list = glob.glob(json_pattern)
        print(file_list)
        for file in file_list:
            with open(file) as data_file:
                self.__contents.extend(json.load(data_file))

    def get_entity_data(self):
        return self.__contents


class LocationManager:
    def __init__(self, location="System/Locations"):
        self.__locations = {}
        self.__active_location = None
        self.data_setup(location)

    def data_setup(self, location):
        self.__active_location = 'Your dormitory room'
        locations = EntityDataReader(location).get_entity_data()
        loc_par = []
        for location in locations:
            location_id = location["location"]
            self.__locations[location_id] = location.copy()
            loc_par.append((location_id, location["parent"]))
        for key in self.__locations:
            location = self.__locations[key]
            nearby_locations = [item[0] for item in loc_par if item[1] == key]
            location["nearby_locations"] = []
            location["nearby_locations"].extend(nearby_locations)
            location["nearby_locations"].append(location["parent"])

    def get_location(self, location):
        return self.__locations[location]

    def get_nearby_locations(self, location):
        return self.__locations[location]["nearby_locations"]

    def get_image(self, location):
        return self.get_location(location)["picture"]

    def print_data(self):
        pprint(self.__locations)

    def set_active_location(self, location):
        self.__active_location = location

    def get_active_location(self):
        return self.__active_location


def main():
    location = LocationManager("Locations")
    location.print_data()
    print(location.get_nearby_locations(location.get_active_location()))


if __name__ == '__main__':
    main()
