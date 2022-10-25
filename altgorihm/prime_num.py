import io
import sys

# 定义标准输入输出
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='UTF8')

isprime = 0
try:
    for k in sys.stdin:
        k = int(k)
        if k > 2:
            for i in range(2, k):
                if k % i == 0:
                    isprime = 0
                    break
                isprime = 1
        elif k == 2:
            isprime = 1

        else:
            isprime = 0

        print(isprime)
except:
    print("输入了空值")
