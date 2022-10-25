'''
编程实现定义两个变量，身高和体重，根据用户输入的身高、体重值，判断一个的身材是否正常：
公式：体重（kg）/（身高（m）的平方值），在18.5～24.9之间属于正常。
输出格式：是否正常：True/False
'''

height = float(input("请输入身高(m):"))

weight = float(input("请输入体重(kg):"))

weightValue = weight / (height ** 2)
if 18.5 < weightValue < 24.9:
    print("是否正常:True")
else:
    print("是否正常:False")
