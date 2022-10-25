import time
scale = 10
print('-' * 10 + '执行开始' + '-' * 10)
for i in range(scale + 1):
    a = (i / scale) * 100
    b = "**" * i
    c = '..' * (scale - i)
    if a == 100:
        print("%{:^3.0f}[{}{}**]".format(a, b, c))
    else:
        print("{:^3.0f}%[{}->{}]".format(a, b, c))
    time.sleep(1)
print('-' * 10 + '执行结束' + '-' * 10)
