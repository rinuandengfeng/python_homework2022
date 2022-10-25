import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n = int(input())
all = 0

while all < n:
    result = 0
    ls = input().split()
    M = float(ls[0])
    m = float(ls[1])
    v = float(ls[2])
    result = (m * v) / ((M - m))
    print("%.6f" % result)
