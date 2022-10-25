import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

# for line in sys.stdin:
n = int(input())
a = 0
sum = 1
if n == 1:
    sum = 2
    print(sum)
else:
    while a < n:
        sum = sum * 2
        a += 1

    print(sum)
# a = 2^31
# print(a)
