from django.test import TestCase

from apps.simc.battle.battle_flow import BattleFlow
# Create your tests here.


class ModelsTest(TestCase):

    def test_event_models(self):
        try:
            battle_flow = BattleFlow(name='test001', monsters=[
                {
                    'id': 'm1',
                    'unit_id': 'goblin',
                    'name': '哥布林',
                    'behavior_script': '>0@dirDamage(2)#1',
                    'max_health': 150,
                    'max_sync': 100,
                    'max_power': 5,
                    'enemy': True
                },
                {
                    'id': 'm2',
                    'unit_id': 'goblin',
                    'name': '哥布林',
                    'behavior_script': '>4@selfHeal(1)#-1',
                    'max_health': 100,
                    'max_sync': 100,
                    'max_power': 5,
                    'enemy': True
                },
                {
                    'id': 'm3',
                    'unit_id': 'ntr',
                    'name': '精英牛头人',
                    'behavior_script': '>4@selfHeal(2)#-1||>0@dirDamage(5)#1',
                    'max_health': 200,
                    'max_sync': 100,
                    'max_power': 5,
                    'enemy': True
                }
            ], character={
                'id': 'ch1',
                'unit_id': 'warrior',
                'name': '勇士',
                'behavior_script': '>0@dirDamage(1)#1||>4@selfHeal(2)#-1',
                'max_health': 100,
                'max_sync': 100,
                'max_power': 5,
                'enemy': False
            }, cards=[
                {
                    'id': 'c1',
                    'card_id': 'pk',
                    'name': '平砍',
                    'behavior_script': '>0@dirDamage(5)#1',
                    'power': 1,
                    'type': 'Spells'  # Spells / Unit
                },
                {
                    'id': 'c2',
                    'card_id': 'zj',
                    'name': '重击',
                    'behavior_script': '>0@dirDamage(10)#1',
                    'power': 2,
                    'type': 'Spells'  # Spells / Unit
                }
            ])

            battle_flow.battle()
            print(battle_flow)
            # 测试gitee和github同步

        except:
            raise SyntaxError

    # def test_guest_models(self):
