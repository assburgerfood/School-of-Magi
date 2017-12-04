from abc import ABCMeta, abstractmethod

NOT_IMPLEMENTED = "You should implement this"


class WorldEntity:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, name):
        self.parent = None
        self.name = name
        self.__picture = None

    @abstractmethod
    def print(self):
        raise NotImplementedError(NOT_IMPLEMENTED)

    def get_picture(self):
        return self.__picture

    def set_picture(self, method, *args):
        if method.lower() in ['yande', 'danbooru', 'gelbooru']:
            print('use API')
            for arg in args:
                print(arg)
        else:
            self.__picture = "System/Pictures/{0}".format(method)


class CompositeEntity(WorldEntity):
    def __init__(self, name):
        super().__init__(name)
        self.entities = {}

    def print(self):
        for entity in self.entities:
            entity.print()

    def add(self, entity):
        self.entities[entity.name] = entity
        self.set_parent(entity)

    def remove(self, entity):
        self.entities.pop(entity.name)

    def set_parent(self, entity):
        self.parent = entity.name


class CompositeArea(CompositeEntity):
    def __init__(self, name):
        super().__init__(name)


class Monster(WorldEntity):
    def __init__(self, name):
        super().__init__(name)

    def print(self):
        print("monster: ", self.name)


class NPC(WorldEntity):
    def __init__(self, name):
        super().__init__(name)

    def print(self):
        print("npc: ", self.name)
