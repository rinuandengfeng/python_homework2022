import time
incomple_sign = 50
print('=' * 23 + '开始下载' + '=' * 25)
for i in range(incomple_sign + 1):
    percentage = (i / incomple_sign) * 100
    completed = "*" * i
    incomplete = '.'*(incomple_sign -i)
    print("{:.0f}%[{}{}]".format(percentage, completed, incomplete))

    time.sleep(0.5)
print('=' * 23 + '执行结束' + '=' * 25)
