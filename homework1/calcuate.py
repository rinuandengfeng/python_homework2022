'''
假设变量 a 为 10, b为 20；
计算(a and b) ；(a or b) ；(not b) 的值；并分析运算结果；
'''

a = 10
b = 20

# and 中含0;均为非0时，返回最后一个值，并集
print(a and b)

# or中,至少有一个非0时，返回第一个非0，交集
print(a or b)
# 若b为True,则not b 为False,若b为False,则not b为True,在python中把默认把0之外的转化为布尔类型为True,0转化为布尔类型为False
print(not b)


