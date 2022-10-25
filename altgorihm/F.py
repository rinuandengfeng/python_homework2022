import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n = int(input())
q = 1
while q < n + 1:
    ls = input()
    a = ls.split()
    if (int(a[0]) == 0) or (int(a[1]) == 0):
        result = 0
        print(result)
    else:
        result = (int(a[0]) + int(a[1])) // 3
        print(result)
    q += 1
