# behave 前处理

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
    behave_list = behave.split("|")
