'''
实现快速计算员工应得奖金的功能。企业发放的奖金根据利润提成：
'''
# 获取利润
profit = float(input("请输入利润(元):"))
get_money = 0
if profit <= 100000:
    get_money = profit * 0.10
elif 100000 < profit <= 200000:
    get_money = 100000 * 0.10 + (profit - 100000) * 0.075
elif 200000 < profit <= 400000:
    get_money = 100000 * 0.10 + 100000 * 0.075 + (profit - 200000) * 0.05
elif 400000 <= profit <= 600000:
    get_money = 100000 * 0.10 + 100000 * 0.075 + 200000 * 0.05 + (profit - 400000) * 0.03
elif 600000 < profit <= 1000000:
    get_money = 100000 * 0.10 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 + (profit - 600000) * 0.015
elif profit > 1000000:
    get_money = 100000 * 0.10 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 + 400000 * 0.015 + \
                (profit - 1000000) * 0.01
else:
    print("输入错误")
print("应发奖金总数为%0.2f元" % get_money)