from System import EntityTypes


class Hero(EntityTypes.CreatureFramework):
    def __init__(self):
        super().__init__(self)

    def new_base(self, health, mana, stamina, strength, magic, gold, sex, name, age):
        self.set_base(health, mana, strength, magic, gold, sex, name)
        self.set_stat_in_base("stamina", stamina)
        self.set_stat_in_base("age", age)

    def refill_stats(self):
        for k, v in self.base.items():
            self.stats[k] = v

    def get_stats_dict(self):
        return self.stats
