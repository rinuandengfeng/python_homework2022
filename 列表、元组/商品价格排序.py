'''
根据商品的价格排序
'''

price = [399, 4369, 539, 288, 109, 749, 235, 190, 99, 1000]
min_price = int(input("请输入最低价:"))
max_price = int(input("请输入最高价:"))
result_price = []
for i in price:
    if min_price <= i <= max_price:
        result_price.append(i)
    else:
        continue
print("1.价格进行升序排列")
print("2.价格进行降序排序")
index_num = int(input("请输入排序:"))
if index_num == 1:
    result_price.sort()
    print(result_price)
elif index_num == 2:
    result_price.sort(reverse=True)
    print(result_price)
else:
    print("输入错误！")
