import argparse

from System import CharBase


class MyGame:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    set_stats_parser = subparsers.add_parser('set stats')
    getter = subparsers.add_parser('get')

    def __init__(self):
        # self.args = self.parser.parse_args()
        self.name = "School of Magi"
        self.player = CharBase.Hero()

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

        self.getter.add_argument('type', choices=['stats', 'base', 'name', 'sex'])

        self.set_stats_parser.set_defaults(func=self.new_game)

        self.getter.set_defaults(func=self.get_data)

    def new_game(self, new_stats):
        print('new game started')
        # self.create_parser()
        self.player.new_base(new_stats["health"], new_stats["mana"], new_stats["stamina"],
                             new_stats["strength"], new_stats["magic"], new_stats["gold"],
                             new_stats["sex"], new_stats["name"], new_stats["age"])
        self.refill_hero_stats()

    def refill_hero_stats(self):
        self.player.refill_stats()

    # --------hero getters-----------
    def get_data(self, data_type):
        switcher = {
            'stats': lambda: self.get_hero_stats(),
            'base': lambda: self.get_hero_base(),
            'name': lambda: self.hero_name(),
            'sex': lambda: self.hero_sex()
        }
        func = switcher.get(data_type, lambda: "nothing")
        return func()

    def get_hero_stats(self):
        print("player stats: ", self.player.stats)
        return self.player.stats

    def get_hero_base(self):
        return self.player.base

    def hero_name(self):
        return self.player.name

    def hero_sex(self):
        return self.player.sex
