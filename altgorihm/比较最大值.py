'''
输入三个数比较最大值
'''

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

try:
    for i in sys.stdin:
        raw = i.split()
        max = int(raw[0])
        for i in range(1, len(raw)):
            if max < int(raw[i]):
                max = int(raw[i])

        print(max)

except:
    print("输入错误")
