# define unit


class MainUnit:

    def __init__(self, unit) -> None:
        self.cur_health = 100,
        self.cur_sync = 100,
        self.name = unit.get('name'),
        self.max_health = 100,
        self.max_sync = 100,
        self.cur_power = 5,
        self.max_power = 5,
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

        pass
