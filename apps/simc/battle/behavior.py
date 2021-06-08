# 单位行为
# behavior类下的所有子方法命名采用驼峰命名，方便策划配置
from apps.simc.models import Monster, Character
from apps.simc.data.unit import MainUnit


class Behavior:

    def __init__(self, behave, target, sender) -> None:
        self.target = MainUnit(target)
        self.player = MainUnit(sender)
        self.behave = behave
        pass

    def dirDamage(self, damage, range):
        """direct damage 直接伤害

        Args:
            damage (integer): 伤害值
            range (integer): 范围
        """
        self.target.cur_health -= damage

    def susDamage(self, damage, range, duration):
        """sustained damage 持续伤害

        Args:
            damage (integer): 伤害值
            range (integer): 范围
            duration (integer): 持续时间
        """


class FeedBack:

    def __init__(self, behave, receiver, source) -> None:
        self.receiver = MainUnit(receiver)
        self.source = MainUnit(source)
        self.behave = behave
        pass

    def feedback(self):
        self.receiver.cur_health -= damage
