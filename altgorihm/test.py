import io
import sys

# 定义变出输出
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

# sys.stdin为标准输入
for line in sys.stdin:
    # 使用split函数进行分割，然后返回一个列表
    a = line.split()
    print(int(a[0]) + int(a[1]))
