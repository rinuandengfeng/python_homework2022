'''
使用*打印三角形
'''

for i in range(9):
    for j in range(9):
        if i >= j:
            print("*",end=" ")
    print()