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
        self.behavior_log = ""
        pass

    def dirDamage(self, level, damage, range=1):
        """direct damage 直接伤害

        Args:
            damage (integer): 伤害值
            range (integer): 范围
        """

        self.behavior_log += f"- 【{self.player}】发起了【{damage}】点dirDamage,目标是【{self.target}】,法术范围【{range}】\n"
        if level == -1:
            this_power = 0
        else:
            this_power = self.power
        self.player.cur_power -= this_power
        self.behavior_log += f"- 【{self.player}】剩余能量【{self.player.cur_power}】\n"

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
        self.behavior_log += f"- 【{self.player}】发起了【{heal}】点selfHeal,目标是【{self.player}】\n"
        if level == -1:
            this_power = 0
        else:
            this_power = self.power
        self.player.cur_power -= this_power
        self.behavior_log += f"- 【{self.player}】剩余能量【{self.player.cur_power}】\n"

    def incDamage(self, increase):
        self.behavior_log += f"- 【{self.player}】发动了【{increase}】点incDamage,目标是【{self.player}】\n"
        self.player.buff.append(
            {
                'type': 'debuff',
                'id': '灼烧id',
                'behavior': '@selfDamage(2)',
                'time': 2,
                'level': 3
            }
        )

    def execute(self, func, *args):
        getattr(self, func)(*args)

        return func, args, self.target, self.player, self.behavior_log


class FeedBack:

    def __init__(self, context, receiver, source, log) -> None:
        self.receiver = receiver
        self.source = source
        self.behave = context
        self.log = log
        pass

    def dirDamage(self, level, damage, range=1):
        """direct damage 直接伤害

        Args:
            damage (integer): 伤害值
            range (integer): 范围
        """

        self.log += f"- 【{self.receiver}】受到了【{damage}】点dirDamage,来源是【{self.source}】,法术范围【{range}】\n"
        if self.receiver.cur_health - damage <= 0:
            self.receiver.cur_health = 0
        else:
            self.receiver.cur_health -= damage
        self.log += f"- 【{self.receiver}】剩余血量【{self.receiver.cur_health}】\n"

    def selfHeal(self, level, heal):
        self.log += f"- 【{self.source}】受到了【{heal}】点selfHeal,来源是【{self.source}】\n"
        if self.source.cur_health + heal > self.source.max_health:
            self.source.cur_health = self.source.max_health
        else:
            self.source.cur_health += heal

        self.log += f"- 【{self.source}】剩余血量【{self.source.cur_health}】\n"

    def execute(self, func, *args):
        getattr(self, func)(*args)
        return self.log


class EventExecutor:
    """
    事件执行器
    """

    def __init__(self, context, target, sender, power=0):
        self.behavior = Behavior(context, target, sender, power)
        self.log = ""

    def execute(self):
        behave_list = self.behavior.behave_list
        for behave in behave_list:
            behave.get('level').extend(behave.get('args'))
            func_name, arguments, target, player, log = self.behavior.execute(behave.get('func'), *behave.get('level'))
            feedback = FeedBack(context={"func": func_name, "args": arguments}, receiver=target, source=player, log=log)
            log = feedback.execute(feedback.behave.get('func'), *feedback.behave.get('args'))
            self.log += log

    def __str__(self):

        return self.log


if __name__ == '__main__':
    event_executor = EventExecutor(context='@dirDamage(1)#1||@selfHeal(2)#-1',
                                   target={'name': '怪物'}, sender={'name': '勇士'}, power=1)
    event_executor.execute()
