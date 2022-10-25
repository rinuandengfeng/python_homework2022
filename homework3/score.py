'''
定义两个整数变量 python_score、c_score，编写代码判断成绩，要求只要有一门成绩 > 60 分就算合格。
'''
# 获取python成绩
python_score = int(input("请输入你的python成绩:"))
# 获取c成绩
c_score = int(input("请输入你的c成绩:"))
# 判断python成绩和c成绩是否至少有一个合格
if python_score > 60 or c_score > 60:
    print('恭喜你，成绩合格~~')
# python成绩和c成绩没有一个合格
else:
    print('很遗憾,你的成绩不合格(ㄒoㄒ)~~')
