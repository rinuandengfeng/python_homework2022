'''
判断用户输入的月份是哪个季节
'''

spring = [3, 4, 5]
summer = [6, 7, 8]
autom = [9, 10, 11]
winter = [12, 1, 2]

month = int(input("请输入当前月份:"))
if month in spring:
    print("{}月是春天".format(month))
elif month in summer:
    print("{}月是夏天".format(month))
elif month in autom:
    print("{}月是秋天".format(month))
elif month in autom:
    print("{}月是冬天".format(month))
else:
    print("输入错误o(╥﹏╥)o")
