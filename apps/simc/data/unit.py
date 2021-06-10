# define unit


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
        self.buff = [{
            'type': 'debuff',
            'id': '灼烧id',
            'behavior': '@selfDamage(2)',
            'time': 2,
            'level': 3
        }, {
            'type': 'debuff',
            'id': '晕眩id',
            'behavior': '@stunned(2)',
            'time': 1,
            'level': 2
        }]
        self.behavior = unit.get('behavior')
        self.enemy = unit.get('enemy')

        pass

    def __str__(self):
        return self.name


class CardUnit:

    def __init__(self, unit):
        self.id = unit.get('id')
        self.name = unit.get('name')
        self.behavior = unit.get('behavior')
        self.power = unit.get('power')
        self.type = unit.get('type')

        pass

    def __str__(self):
        return self.name