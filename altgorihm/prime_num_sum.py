import io
import sys

# 定义标准输入输出
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='UTF8')

try:
    for i in sys.stdin:
        prime_num = []
        a = i.split()
        if int(a[0]) > int(a[1]):
            for j in range(int(a[1]), (int(a[0]) + 1)):
                if j > 1:
                    if j <= 2:
                        prime_num.append(j)
                        continue
                    else:
                        for k in range(2, j):
                            if j % k == 0:
                                break
                        else:
                            prime_num.append(j)
                else:
                    continue
            if len(prime_num) != 0:
                for num in prime_num:
                    print(num, end=" ")
                print()
            else:
                print("Not Found.")
        else:
            for j in range(int(a[0]), (int(a[1]) + 1)):
                if j > 1:
                    if j <= 2:
                        prime_num.append(j)
                        continue
                    else:
                        for k in range(2, j):
                            if j % k == 0:
                                break
                        else:
                            prime_num.append(j)
                else:
                    continue
            if len(prime_num) != 0:
                for num in prime_num:
                    print(num, end=" ")
                print()
            else:
                print("Not Found.")
except:
    print("输入值为空")
