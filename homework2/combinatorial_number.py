"""
四个数字1、2、3、4组成多少个互不相同且无重复数字的三位数，有多少个
"""
row = [1, 2, 3, 4]
# 定义空列表，存放组成的符合要求数
total_num = []
# 遍历百位的值
for i in row:
    # 遍历十位的值
    for j in row:
        # 和百位数相同的给去掉
        if i == j:
            continue
        # 获取个位的值
        for k in row:
            # 和百位或者十位相同的数去掉
            if k == i or k == j:
                continue
            # 计算出组成的三位数
            num = i * 100 + j * 10 + k
            print(num, end=" ")
            # 将组成的数放到数组中,后面计算一共组成的个数
            total_num.append(num)
print()
print("一共组成%d个互不相同且无重复数字的三位数" % len(total_num))
