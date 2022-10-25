'''
重复列表元素
输出结果为' I have fentiao, fendai, fensi and apple.'
'''

names = [' fentiao', ' fendai', ' fensi', ' apple']

# 使用join函数，将列表中的元素按照指定字符进行分割
print("I have " + ','.join(names[:3]) + "and" + names[-1] + ".")
