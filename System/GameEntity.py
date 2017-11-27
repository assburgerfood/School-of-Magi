from abc import ABCMeta, abstractmethod

NOT_IMPLEMENTED = "You should implement this"


class WorldEntity:
    __metaclass__ = ABCMeta

    @abstractmethod
    def print(self):
        raise NotImplementedError(NOT_IMPLEMENTED)


class CompositeEntity(WorldEntity):
    def __init__(self):
        self.entities = []

    def print(self):
        for entity in self.entities:
            entity.print()

    def add(self, entity):
        self.entities.append(entity)

    def remove(self, entity):
        self.entities.remove(entity)


class Monster(WorldEntity):
    def __init__(self, name):
        self.name = name

    def print(self):
        print("monster: ", self.name)


class NPC(WorldEntity):
    def __init__(self, name):
        self.name = name

    def print(self):
        print("npc: ", self.name)
