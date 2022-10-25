'''
利用成员运算符判断某个元素是否在指定序列：例，a的值为10，判断其是否在列表list = [1,2,3,4,5]中，
若在，返回“10在list列表中”，否则，返回“10不在list列表中。”
'''

a = 10
# 生成默认列表
list = [1, 2, 3, 4, 5]

if a in list:
    print("{}在list列表中".format(a))
else:
    print("{}不在list列表中".format(a))
