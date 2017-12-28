class ProgressData:
    def __init__(self):
        self.__data = {}

    def save_data_array(self, key, data=None):
        if key not in self.__data:
            self.__data[key] = []
        if data is not None and data not in self.__data[key]:
            self.__data[key].append(data)

    def get_data_array(self, key):
        if key in self.__data:
            return self.__data[key]
        else:
            return None
