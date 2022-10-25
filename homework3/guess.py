'''
实现“石头、剪刀、布”游戏。在游戏规则中，石头胜剪刀，剪刀胜布、布胜石头。
'''
import random

content = int(input("请输入您出的拳 石头(1)/剪刀(2)/布(3):"))
# 产生随机数
reslut = random.randint(1, 3)
if reslut == content:
    print("心有灵犀，再来一盘！")
else:
    print("我不服，再来一盘！")
    while True:
        content = int(input("请输入您出的拳 石头(1)/剪刀(2)/布(3):"))
        if reslut == content:
            print("耶！我赢啦！")
            break
        else:
            print("我不服，再来一盘！")
            continue
