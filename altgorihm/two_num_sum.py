'''
求两数的和
'''

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

try:
    for i in sys.stdin:
        a = i.split()
        total = int(a[0]) + int(a[1])
        print(total)
except:
    print("输入错误")
