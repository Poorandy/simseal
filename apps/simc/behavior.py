# 单位行为
# behavior类下的所有子方法命名采用驼峰命名，方便策划配置

class Behavior:

    def __init__(self) -> None:
        self.target = {}
        pass

    def dirDamage(self, damage, range):
        """direct damage 直接伤害

        Args:
            damage (integer): 伤害值
            range (integer): 范围
        """

    def susDamage(self, damage, range, duration):
        """sustained damage 持续伤害

        Args:
            damage (integer): 伤害值
            range (integer): 范围
            duration (integer): 持续时间
        """
