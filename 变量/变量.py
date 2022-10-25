# 变量的定义,动态数据类型，不需要先定义数据类型
a = 123

print(a)
print(type(a))


# 函数也可以赋值给变量
def test():
    print(a)


x = test

print(type(x))





