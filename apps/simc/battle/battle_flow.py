# 战斗流程
import random

from apps.simc.battle.preprocess import preprocess
from apps.simc.battle.event import EventExecutor
from apps.simc.data.unit import MainUnit, CardUnit


# todo: 费用没有用完；卡牌墓地


class BattleFlow:
    """
    战斗流
    """

    def __init__(self, name, monsters: list, character: dict, cards: list, loop=100):
        self.round = 0
        self.battle_name = name
        self.monsters = {monster.get('id'): MainUnit(monster)
                         for monster in monsters}
        self.cards = {card.get('id'): CardUnit(card) for card in cards}
        self.character = MainUnit(character)
        self.all_units = {**self.monsters, **
                          {self.character.id: self.character}}
        self.game_over = False
        self.battle_log = ""

    def battle(self):
        self.character.cur_power = self.character.max_power
        self.round += 1
        self.battle_log += f"*-----------Round {self.round}-----------*\n"
        # 玩家先攻
        sender = self.character  # 事件执行器发送者
        # 先用卡牌
        # 随机选卡
        card = random.choices(list(self.cards.values()))[0]
        context = card.behavior
        power = card.power
        target = self.get_target(context, sender)
        self.battle_log += f"- *** 【{sender}】使用卡牌 【{card}】 ***\n"
        event_executor = EventExecutor(context, target, sender, power)
        event_executor.execute()
        self.battle_log += event_executor.__str__()
        if not self.check_game_over():
            # 再用被动
            self.battle_log += f"- *** 【{sender}】使用被动 ***\n"
            context = sender.behavior
            for ctx in context.split('||'):
                target = self.get_target(ctx, sender)
                event_executor = EventExecutor(ctx, target, sender)
                event_executor.execute()
                self.battle_log += event_executor.__str__()

            # 怪物回合
            for sender in list(self.monsters.values()):
                if sender.cur_health and not self.check_game_over():
                    self.battle_log += f"- *** 【{sender}】使用被动 ***\n"
                    context = sender.behavior
                    for ctx in context.split('||'):
                        target = self.get_target(ctx, sender)
                        event_executor = EventExecutor(ctx, target, sender)
                        event_executor.execute()
                        self.battle_log += event_executor.__str__()

        if not self.check_game_over():
            self.battle()
        else:
            self.battle_log += 'Game Over'
            return 0

    def check_game_over(self):
        if not sum([x.cur_health for x in self.monsters.values()]):  # 怪物当前生命值全0
            self.game_over = True
        elif not self.character.cur_health:
            self.game_over = True

        return self.game_over

    def get_target(self, behave, sender):
        res = preprocess(behave)[0]
        target_flag = res.get('target')
        if not target_flag:  # 敌方所有存活单位
            target = random.choices(
                list(dict(filter(lambda elem: elem[1].cur_health != 0 and elem[1].enemy != sender.enemy,
                                 self.all_units.items())).values()))[0]
        elif target_flag == 1:  # 敌方所有单位
            target = random.choices(
                list(dict(filter(lambda elem: elem[1].enemy != sender.enemy, self.all_units.items())).values()))[
                0]
        elif target_flag == 2:  # 友方所有存活单位
            target = random.choices(
                list(dict(filter(lambda elem: elem[1].cur_health != 0 and elem[1].enemy == sender.enemy,
                                 self.all_units.items())).values()))[0]
        elif target_flag == 3:  # 友方所有单位
            target = random.choices(
                list(dict(filter(lambda elem: elem[1].enemy == sender.enemy, self.all_units.items())).values()))[
                0]
        elif target_flag == 4:
            target = sender
        else:
            target = None

        return target

    def __str__(self):
        return self.battle_log


if __name__ == '__main__':
    for i in range(1):
        try:
            battle_flow = BattleFlow(battle_id='1', monsters=[
                {
                    'id': 'm1',
                    'name': '哥布林',
                    'behavior': '>0@dirDamage(2)#1',
                    'max_health': 150,
                    'max_sync': 100,
                    'max_power': 5,
                    'enemy': True
                },
                {
                    'id': 'm2',
                    'name': '回血史莱姆',
                    'behavior': '>4@selfHeal(1)#-1',
                    'max_health': 100,
                    'max_sync': 100,
                    'max_power': 5,
                    'enemy': True
                },
                {
                    'id': 'm3',
                    'name': '精英牛头人',
                    'behavior': '>4@selfHeal(2)#-1||>0@dirDamage(5)#1',
                    'max_health': 200,
                    'max_sync': 100,
                    'max_power': 5,
                    'enemy': True
                }
            ], character={
                'id': 'ch1',
                'name': '勇士',
                'behavior': '>0@dirDamage(1)#1||>4@selfHeal(2)#-1',
                'max_health': 100,
                'max_sync': 100,
                'max_power': 5,
                'enemy': False
            }, cards=[
                {
                    'id': 'c1',
                    'name': '平砍',
                    'behavior': '>0@dirDamage(5)#1',
                    'power': 1,
                    'type': 'Spells'  # Spells / Unit
                },
                {
                    'id': 'c2',
                    'name': '重击',
                    'behavior': '>0@dirDamage(10)#1',
                    'power': 2,
                    'type': 'Spells'  # Spells / Unit
                }
            ])

            battle_flow.battle()

        except:
            raise SyntaxError
