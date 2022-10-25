'''
计算合小于10000的最大整数
'''
n = 1
total = 0
while total <= 10000:
    total += n
    n += 1

print("满足条件的最大整数为:{}".format(n - 2))
