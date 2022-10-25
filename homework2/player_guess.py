'''
程序随机产生一个 0~300之间的整数， 玩家竞猜，若猜中则提
示Bingo，若猜大了提示Too large，否则提示 Too small。
'''
# 导入随机数模块包
from random import randint

num = int(input("请输入一个整数:"))
# 生成一个随机整数
x = randint(0, 300)
# 判断是否猜对了
if num == x:
    print("Bingo")
# 判断是否猜大了
elif num > x:
    print("Too large")
# 否则就是猜小了
else:
    print("Too small")
