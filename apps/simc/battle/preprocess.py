# behave 前处理
import json
import re

p1 = re.compile(r'[(](.*?)[)]', re.S)
p2 = re.compile(r'[>](.*?)[@]', re.S)
p3 = re.compile(r'[@](.*?)[(]', re.S)


def preprocess(behave):
    """behave前处理
    >0@susDamage(2)#1||>4@selfHeal(2)#-1||>0@dirDamage(1)#-1
    @: behave func 方法定义符
    #：behave level 优先级定义符
       -1 : 被动（回合结束时触发）
       -2 : unit初始化的状态条
       0-99 : less and faster
    >: behave target 目标类型定义符
       0:敌对非死亡单位
       1:敌对所有单位
       2:友方非死亡单位
       3:友方所有单位
       4:自己


    Args:
        behave (string): 命令
    """
    behave = ''.join(behave.split())
    behave_list = behave.split("||")

    proceed = [
        {
            'func': re.findall(p3, x)[0],
            'target': int(re.findall(p2, x)[0]),
            'level': [int(x.split('#')[1])],
            'args': [int(y) for y in re.findall(p1, x)[0].split(',')]
        }
        for x in behave_list
    ]

    return proceed


if __name__ == '__main__':
    behave = '>0@susDamage(2)#1||>4@selfHeal(2)#-1||>0@dirDamage(1)#-1'
    res = preprocess(behave)
    print(json.dumps(res, ensure_ascii=False, indent=2))
