n = int(input())
total = ""
if n != 0:
    while (n > 0):
        # 获取二进制值
        binary = n % 2
        n = n // 2
        total = str(binary) + total
else:
    total = 0

print(total)
