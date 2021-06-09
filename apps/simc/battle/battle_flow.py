# 战斗流程

import django

import os
import json
import sys
import random

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ['DJANGO_SETTINGS_MODULE'] = 'simseal.settings'
django.setup()

from apps.simc.data.unit import MainUnit
from apps.simc.battle.behavior import EventExecutor

# todo: 玩家还会对死亡的单位进行攻击，但是可以选中尸体；费用没有用完；卡牌墓地；怪物的目标


class BattleFlow:
    """
    战斗流
    """

    def __init__(self, battle_id, monsters: list, character: dict, cards: list):
        self.round = 0
        self.battle_id = battle_id
        self.monsters = {monster.get('id'): MainUnit(monster) for monster in monsters}
        self.cards = {card.get('id'): card for card in cards}
        self.character = MainUnit(character)
        self.game_over = False

    def battle(self):
        self.character.cur_power = self.character.max_power
        if self.game_over:
            print('Game Over')
            return 0
        elif not sum([x.cur_health for x in self.monsters.values()]):  # 怪物当前生命值全0
            print('Win !')
            self.game_over = True
        elif not self.character.cur_health:
            print('Lose !')
            self.game_over = True
        else:
            self.round += 1
            print(f"*-----------Round {self.round}-----------*")
            # 玩家先攻
            sender = self.character  # 事件执行器发送者
            # 先用卡牌
            # 随机选卡
            target = random.choices(list(self.monsters.values()))[0]
            card = random.choices(list(self.cards.values()))[0]
            context = card.get('behavior')
            power = card.get('power')

            print(f"- *** 【{sender}】使用卡牌 【{card.get('name')}】 ***")
            event_executor = EventExecutor(context, target, sender, power)
            event_executor.execute()

            # 再用被动
            print(f"- *** 【{sender}】使用被动 ***")
            target = random.choices(list(self.monsters.values()))[0]
            context = sender.behavior
            event_executor = EventExecutor(context, target, sender)
            event_executor.execute()

            # 怪物回合
            for sender in list(self.monsters.values()):
                if sender.cur_health:
                    print(f"- *** 【{sender}】使用被动 ***")
                    target = self.character
                    context = sender.behavior
                    event_executor = EventExecutor(context, target, sender)
                    event_executor.execute()
        self.battle()
        pass


if __name__ == '__main__':
    battle_flow = BattleFlow(battle_id='1', monsters=[
        {
            'id': 'm1',
            'name': '哥布林',
            'behavior': '@dirDamage(2)#1',
            'max_health': 150,
            'max_sync': 100,
            'max_power': 5,
        },
        {
            'id': 'm2',
            'name': '回血史莱姆',
            'behavior': '@selfHeal(1)#-1',
            'max_health': 100,
            'max_sync': 100,
            'max_power': 5,
        }
    ], character={
        'id': 'ch1',
        'name': '勇士',
        'behavior': '@dirDamage(1)#1||@selfHeal(2)#-1',
        'max_health': 100,
        'max_sync': 100,
        'max_power': 5,
    }, cards=[
        {
            'id': 'c1',
            'name': '平砍',
            'behavior': '@dirDamage(5)#1',
            'power': 1,
            'type': 'Spells'  # Spells / Unit
        },
        {
            'id': 'c2',
            'name': '重击',
            'behavior': '@dirDamage(10)#1',
            'power': 2,
            'type': 'Spells'  # Spells / Unit
        }
    ])
    battle_flow.battle()
