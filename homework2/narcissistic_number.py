"""
求100~1000内的水仙花数
"""
# 遍历100~1000内的所有数
for i in range(100, 1000):
    # 各位数
    unit = i % 10
    # 十位数
    tens_digit = (i // 10) % 10
    # 百位数
    hundreds_digit = (i // 100) % 10
    # 计算每个位上的数字的3次幂之和
    target_num = unit ** 3 + tens_digit ** 3 + hundreds_digit ** 3
    # 判断每个位上的数字的3次幂是否与原值相等
    if target_num == i:
        print(target_num)
