import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
n = int(input())

ls = input().split()
L = int(ls[0])
R = int(ls[1])

hi = input().split()
hi_max = int(hi[0])
max = int(ls[0])
for i in range(L, R + 1):
    if max < i:
        max = i

for i in hi:
    if hi_max < int(i):
        hi_max = int(i)
sh = max
if max <= hi_max:
    sh = max + max
elif max > hi_max:
    sh = hi_max + max

print(int(sh))
