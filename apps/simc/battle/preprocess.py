# behave 前处理
import json
import re


p1 = re.compile(r'[(](.*?)[)]', re.S)

def preprocess(behave):
    """behave前处理
    @susDamage(2)#1||@selfHeal(2)#-1||@dirDamage(1)#-1
    @: behave func 方法定义符
    #：behave level 优先级定义符
       -1 : 被动
       0-99 : less and faster

    Args:
        behave (string): 命令
    """
    behave = ''.join(behave.split())
    behave_list = behave.split("||")

    proceed = [
        {
            'func': x.split('#')[0][1:].split('(')[0],
            'level': [int(x.split('#')[1])],
            'args': [int(y) for y in re.findall(p1, x)[0].split(',')]
        }
        for x in behave_list
    ]

    return proceed


if __name__ == '__main__':
    behave = '@susDamage(2)#1||@selfHeal(2)#-1||@dirDamage(1)#-1'
    res = preprocess(behave)
    print(json.dumps(res, ensure_ascii=False, indent=2))
