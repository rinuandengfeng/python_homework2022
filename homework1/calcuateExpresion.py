'''
输入一个数字x传入表达式 (x+10)*8/2//3%10 后对结果求三次方 输出结果(输入和输出要有提示)；
'''

import math

x = int(input("请输入一个数字:"))

# 计算表达式的结果
result = (x + 10) * 8 / 2 // 3 % 10

# 得到表示式的三次方
result = math.pow(result, 3)

print("输出的结果为：", result)
