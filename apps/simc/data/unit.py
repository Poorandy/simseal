# define unit
from apps.simc.battle.preprocess import preprocess


class MainUnit:

    def __init__(self, unit) -> None:
        self.id = unit.get('id')
        self.cur_health = unit.get('max_health')
        self.cur_sync = unit.get('max_sync')
        self.name = unit.get('name')
        self.max_health = unit.get('max_health')
        self.max_sync = unit.get('max_sync')
        self.cur_power = unit.get('max_power')
        self.max_power = unit.get('max_power')
        self.behavior = unit.get('behavior_script')
        self.buffs, self.debuffs = self.generate_buffs()
        self.enemy = unit.get('enemy')

        pass

    def __str__(self):
        return self.name

    def generate_buffs(self):
        behaves = list(filter(lambda elem: elem.get('level')
                       [0] == -2, preprocess(self.behavior)))

        return "buffs", "debuffs"
        pass


class CardUnit:

    def __init__(self, unit):
        self.id = unit.get('id')
        self.name = unit.get('name')
        self.behavior = unit.get('behavior_script')
        self.power = unit.get('power')
        self.type = unit.get('type')

        pass

    def __str__(self):
        return self.name


if __name__ == '__main__':
    unit = MainUnit({
        'id': 'm3',
        'name': '精英牛头人',
        'behavior_script': '>4@selfHeal(2)#-1||>0@dirDamage(5)#1||>0@incDamage(1)#-2',
        'max_health': 200,
        'max_sync': 100,
        'max_power': 5,
        'enemy': True
    })
    print(unit.buffs)
