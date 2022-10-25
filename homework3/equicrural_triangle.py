'''
打印等腰三角形
'''

for i in range(9):
    print(" " * (9 - i), end=" ")
    for j in range(9):
        if i >= j:
            print("*", end=" ")
    print()
