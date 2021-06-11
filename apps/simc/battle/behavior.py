# 单位行为-单位反馈
# 战斗流程的最小单位
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

    def __init__(self, context, target, sender, power=0) -> None:
        self.target = target
        self.player = sender
        self.behave_list = preprocess(context)
        self.power = power
        pass

    def dirDamage(self, level, damage, range=1):
        """direct damage 直接伤害

        Args:
            damage (integer): 伤害值
            range (integer): 范围
        """

        print(f"- 【{self.player}】发起了【{damage}】点dirDamage,目标是【{self.target}】,法术范围【{range}】")
        if level == -1:
            this_power = 0
        else:
            this_power = self.power
        self.player.cur_power -= this_power
        print(f"- 【{self.player}】剩余能量【{self.player.cur_power}】")

    def susDamage(self, level, damage, range, duration):
        """sustained damage 持续伤害

        Args:
            damage (integer): 伤害值
            range (integer): 范围
            duration (integer): 持续时间
        """
        if level == -1:
            self.power = 0

    def selfHeal(self, level, heal):
        print(f"- 【{self.player}】发起了【{heal}】点selfHeal,目标是【{self.player}】")
        if level == -1:
            this_power = 0
        else:
            this_power = self.power
        self.player.cur_power -= this_power
        print(f"- 【{self.player}】剩余能量【{self.player.cur_power}】")

    def execute(self, func, *args):
        getattr(self, func)(*args)

        return func, args, self.target, self.player


class FeedBack:

    def __init__(self, context, receiver, source) -> None:
        self.receiver = receiver
        self.source = source
        self.behave = context
        pass

    def dirDamage(self, level, damage, range=1):
        """direct damage 直接伤害

        Args:
            damage (integer): 伤害值
            range (integer): 范围
        """

        print(f"- 【{self.receiver}】受到了【{damage}】点dirDamage,来源是【{self.source}】,法术范围【{range}】")
        if self.receiver.cur_health - damage <= 0:
            self.receiver.cur_health = 0
        else:
            self.receiver.cur_health -= damage
        print(f"- 【{self.receiver}】剩余血量【{self.receiver.cur_health}】")

    def selfHeal(self, level, heal):
        print(f"- 【{self.source}】受到了【{heal}】点selfHeal,来源是【{self.source}】")
        if self.source.cur_health + heal > self.source.max_health:
            self.source.cur_health = self.source.max_health
        else:
            self.source.cur_health += heal

        print(f"- 【{self.source}】剩余血量【{self.source.cur_health}】")

    def execute(self, func, *args):
        getattr(self, func)(*args)


class EventExecutor:
    """
    事件执行器
    """

    def __init__(self, context, target, sender, power=0):
        self.behavior = Behavior(context, target, sender, power)

    def execute(self):
        behave_list = self.behavior.behave_list
        for behave in behave_list:
            behave.get('level').extend(behave.get('args'))
            func_name, arguments, target, player = self.behavior.execute(behave.get('func'), *behave.get('level'))
            feedback = FeedBack(context={"func": func_name, "args": arguments}, receiver=target, source=player)
            feedback.execute(feedback.behave.get('func'), *feedback.behave.get('args'))


if __name__ == '__main__':
    event_executor = EventExecutor(context='@dirDamage(1)#1||@selfHeal(2)#-1',
                                   target={'name': '怪物'}, sender={'name': '勇士'}, power=1)
    event_executor.execute()