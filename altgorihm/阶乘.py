'''
求一个数的阶乘
'''

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

try:
    for i in sys.stdin:
        n = int(i)
        total = 0
        raw = 1
        if n == 0:
            total = 1
        else:
            for j in range(1, n + 1):
                for k in range(1, j + 1):
                    raw *= k
                total += raw
                raw = 1
        print(total)
except:
    print("输入错误")
