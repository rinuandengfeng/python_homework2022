'''
100块钱买多少只公鸡、母鸡、雏鸡
'''
# 钱
money = 100

total_chicken = 100
for cock in range(1, 21):
    for hen in range(1, 34):
        for biddy in range(3, 100, 3):
            # 判断数量之和钱数之和都等于100
            if (cock + hen + biddy == 100) and ((cock * 5) + (hen * 3) + (biddy / 3)) == money:
                print('买公鸡:{}只,买母鸡:{}只，买雏鸡:{}只'.format(cock, hen, biddy))
