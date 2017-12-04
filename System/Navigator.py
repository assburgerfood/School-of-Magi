class Navigator:
    def __init__(self, entity_manager):
        self.__location = None

    def set_location(self, location):
        self.__location = location
