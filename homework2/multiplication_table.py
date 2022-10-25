"""
打印九九乘法表
"""

for i in range(1, 10):
    for j in range(1, i + 1):
        # print函数中的end可以自定义结尾的格式,默认换行
        print("{} * {} = {}\t".format(i, j, i * j), end=" ")
    # print函数默认也是打印换行
    print()
print("九九乘法表输出完成(￣▽￣)")
