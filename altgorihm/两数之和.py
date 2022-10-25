import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

for line in sys.stdin:
    a = line.split()
    sum = int(a[0]) +int(a[1])
    print(sum)