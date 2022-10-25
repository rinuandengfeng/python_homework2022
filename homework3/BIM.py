'''
体质量指数
'''
# 接收体重
weigth = float(input("请输入你的体重(kg):"))
# 接收身高
height = float(input("请输入身高(m):"))
# 计算bmi指数
bmi = weigth / (height ** 2)
# 判断bmi值
if bmi < 18.5:
    print("您属于过轻")
elif 18.5 <= bmi <= 23.9:
    print("您属于正常")
elif 24 <= bmi <= 27:
    print("您属于过重")
elif 28 <= bmi <= 32:
    print("您属于肥胖")
else:
    print("您属于非常肥胖")
