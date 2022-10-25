import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
all = 1

# 获取测试用例
t = int(input())

while all < t:
    a = input().split()
    d = (int(a[1]) - int(a[0]))/2
    n = int(a[2])
    sum = n*int(a[0]) + (n *(n-1)*d)/2
    print(int(sum))


