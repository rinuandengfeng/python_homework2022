'''
 输入一个数判断它是否在列表[1, '二', 3.1, True]中
'''

sz = [1, '二', 3.1, True]

a = input('请输入一个值:')

for i in sz:
    if a == str(i):
        print('{}在列表中'.format(a))
        # 退出程序
        exit()
# 没有在列表中打印出不在列表中
print('{}不在列表中'.format(a))
