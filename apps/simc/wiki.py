# 前端返回：
monster_list = [
    {
        'id': '',
        'name': '',
        'behavior': '',
        'hp': 100,
        'sync': 100
    }
] > list(dict)

card_list = [
    {
        'id': '',
        'name': '',
        'behavior': '@dirDamage(5)',
        'power': 1,
        'type': 'Spells'  # Spells / Unit
    }
] > list(dict)

character = {
    'id': '',
    'name': '',
    'behavior': '',
    'hp': 100,
    'sync': 100
} > dict

battle_field = 'id' > str

run_number = 100

# 近似  [1,2,3,4,5]  shuffle [5,2,1,4,3] target
# 后端接收

# case：
# 斩杀
## AOE - 打他range范围内的其他单位
# 身上有DOT，不对他使用卡牌
# buff类卡牌，优先使用

