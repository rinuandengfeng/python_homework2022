'''
任意输入两个整型或浮点数，并对其(随便选一个比较运算符)进行比较操作
'''

one = int(input("请输入第一个整数："))

two = int(input("请输入第二个整数："))

if one > two:
    print("两个数中最大值为:", one)
elif one < two:
    print("两个数中最大值为:", two)
else:
    print("两个数相等，均为:", one)
