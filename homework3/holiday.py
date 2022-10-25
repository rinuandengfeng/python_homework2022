# 导入random
import random

holiday_name = input('请输入今天的节日:')
# 判断今天是不是情人节
if holiday_name == '情人节':
    #定义随机范围数组
    program = ['买玫瑰', '看电影']
    # 随机从列表中抽取一个
    print(random.choice(program))
# 判断今天是平安夜
elif holiday_name == '平安夜':
    # 定义随机范围数组
    program = ['买苹果', '吃大餐']
    # 随机从列表中抽取一个
    print(random.choice(program))
# 判断今天是不是她的生日
elif holiday_name == '生日':
    print('买蛋糕')
# 其他节日
else:
    print('吃面条')
