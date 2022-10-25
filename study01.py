# """
# 这是多行注释
# 输出：print()
# 输入：
# 查看数据类型的函数： type()
# 整型    int long short
# 浮点型   float double
# 字符串
# """
#
# # 单行注释
# '''
# 这是多行注释
# '''
# # 单行注释
# """
# 这是多行注释
# """
#
#
# # 这是一个求和函数
# def sums(a, b):
#     print(a + b)
#     return a + b
#
#
# print("hello world")
# # 这是单行注释
# print(type("hello,world"))
# print("-" * 100)
# print(3 + 5)
# print(type(3 + 5))
#
# print("-" * 20)
# type(3 + 4)
#
# print("-" * 20)
# # 复数
# a = complex(1.2, 4.2)
#
# print(a)
#
# x = 1.0
# y = 2
# print(type(x))
# print(type(y))
#
# # 布尔类型
# print("-" * 20)
# print(type(True))
# print(type(False))
#
# print("-" * 20)
#
# # 字符串类型
# z = '哈哈哈哈'
# y = '我是美女'
# # print("哈哈哈哈")
# # print('我是帅哥')
#
# print('z')
# print(z)
# print(type(z))
# print(type(y))
#
# lis1 = [1, 3, 2]
#
# print(id(lis1))
# lis2 = lis1
# print(id(lis2))
#
#
# lis = ['apple','lemon','pear','peach']
#
# def fn(x):
#
#     return x[::-1]
# print(fn)
# lis.sort(key=fn,reverse=True)
# print(lis)

def chanageList(nums):
    nums.append('c')
    print(id(nums))
    print("nums", nums)
str1 = ['a', 'b']
# 调用函数
chanageList(str1)
print(id(str1))
print("str1", str1)

strs = 'abbacabb'

print(id(strs))
x  = strs.strip('ab')
print(x)
print(id(x))
print(strs.strip('b'))