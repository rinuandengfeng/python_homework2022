'''
实现删除列表中的重复元素
'''
raw_list = list()
length = int(input("请输入列表的总个数:"))
i = 0
while i < length:
    element = input('请输入第{}元素:'.format(i + 1))
    raw_list.append(element)
    i += 1
# 去除重复元素
list = set(raw_list)
print(list)
