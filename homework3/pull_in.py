'''
模拟乘客乘地铁进站流程。
坐地铁的实际情况是：先检查是否有车票，然后进行安检，安检通过才能进站。
'''
# 车票
fare = input("有车票输入y，否则输入n:")

# 判断是否有车票
if fare == 'y':
    print('有车票，可以进站')
    risk_good = int(input('携带有危险物品输入1，否则输入0:'))
    # 判断是携带危险物品
    if risk_good == 1:
        print('没通过安检')
        print('不能乘车')
    else:
        print('通过安检')
else:
    print('没有车票，不能进站')
