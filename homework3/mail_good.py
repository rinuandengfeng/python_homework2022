'''
快递寄件不同地区的寄件价格不一样
'''
# 获取地区
addid = input("请输入地区编号（01、02、03）:")
# 获取物品重量
weight = float(input("请输入物品重量(kg):"))
# 定义付费金额变量
total_money = 0
if addid == '01':
    # 判断商品的重量
    if 0 < weight <= 2:
        total_money = 13
    elif weight > 2:
        total_money = 13 + (weight - 2) * 3
    else:
        print("请输入正确的数重量")
    print('您需要支付%.2f元' % total_money)
elif addid == '02':
    # 判断商品的重量
    if 0 < weight <= 2:
        total_money = 12
    elif weight > 2:
        total_money = 12 + (weight - 2) * 2
    else:
        print("请输入正确的数重量")
    # 输出支付的金额
    print('您需要支付%.2f元' % total_money)
elif addid == '03':
    # 判断商品的重量
    if 0 < weight <= 2:
        total_money = 14
    elif weight > 2:
        total_money = 14 + (weight - 2) * 4
    else:
        print("请输入正确的数重量")
    print('您需要支付%.2f元' % total_money)
else:
    print("输入错误┭┮﹏┭┮")
