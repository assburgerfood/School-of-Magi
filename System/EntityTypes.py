class CreatureFramework:
    base = {}
    stats = {}
    name = ""
    sex = ""

    def __init__(self, health=0, mana=0, strength=0, magic=0, gold=0, sex=None, name=None):
        self.base["health"] = health
        self.base["mana"] = mana
        self.base["strength"] = strength
        self.base["magic"] = magic
        self.base["gold"] = gold
        self.sex = sex
        self.name = name

    def set_stat_in_base(self, name, stat):
        self.base[name] = stat

    def set_base(self, health, mana, strength, magic, gold, sex, name):
        self.set_stat_in_base("health", health)
        self.set_stat_in_base("mana", mana)
        self.set_stat_in_base("strength", strength)
        self.set_stat_in_base("magic", magic)
        self.set_stat_in_base("gold", gold)
        self.name = name
        self.sex = sex
