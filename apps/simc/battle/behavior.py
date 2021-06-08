# 单位行为
# behavior类下的所有子方法命名采用驼峰命名，方便策划配置

import sys
import os
import django

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ['DJANGO_SETTINGS_MODULE'] = 'simseal.settings'
django.setup()

from apps.simc.models import Monster, Character
from apps.simc.data.unit import MainUnit
from apps.simc.battle.preprocess import preprocess


class Behavior:

    def __init__(self, behave, target, sender, power=0) -> None:
        self.target = MainUnit(target)
        self.player = MainUnit(sender)
        self.behave_list = preprocess(behave)
        self.power = power
        pass

    def dirDamage(self, level, damage, range=1):
        """direct damage 直接伤害

        Args:
            damage (integer): 伤害值
            range (integer): 范围
        """


        print(f"发起了{damage}点dirDamage,目标是{self.target.name},法术范围{range}")
        if level == -1:
            this_power = 0
        else:
            this_power = self.power
        self.player.cur_power -= this_power
        print(f"剩余能量{self.player.cur_power}")

    def susDamage(self, level, damage, range, duration, power=0):
        """sustained damage 持续伤害

        Args:
            damage (integer): 伤害值
            range (integer): 范围
            duration (integer): 持续时间
        """
        if level == -1:
            self.power = 0

    def selfHeal(self, level, heal):
        print(f"发起了{heal}点selfHeal,目标是{self.player.name}")
        if level == -1:
            this_power = 0
        else:
            this_power = self.power
        self.player.cur_power -= this_power
        print(f"剩余能量{self.player.cur_power}")

    def execute(self, func, *args):
        getattr(self, func)(*args)


class FeedBack:

    def __init__(self, behave, receiver, source) -> None:
        self.receiver = MainUnit(receiver)
        self.source = MainUnit(source)
        self.behave = behave
        pass

    def execute(self, func, *args):
        getattr(self, func)(*args)


if __name__ == '__main__':
    behavior = Behavior(behave='@selfHeal(2)#-1||@dirDamage(1)#1',
                        target={'name': 'target'}, sender={'name': 'sender'}, power=1)
    behave_list = behavior.behave_list
    for behave in behave_list:
        behave.get('level').extend(behave.get('args'))
        behavior.execute(behave.get('func'), *behave.get('level'))
