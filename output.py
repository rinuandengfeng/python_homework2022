
# from functools import total_ordering
# from this import d


# age = 10

# print("我今年%d岁" % age)

# # 年龄加一岁
# age += 1
# print("我今年%d岁" % age)


# # 练习题
# name = "chris"
# QQ = 1061747240
# tele = 15239330590
# company = "上海玉带科技有限公司"

# print("========我的名片========\n")
# print("姓名:%s\n" % name)
# print("QQ:%d\n" % QQ)
# print("手机号:%d\n" % tele)
# print("公司地址:%s\n" % company)
# print("========================")


# a = 1024 * 768
# print("1024 * 768 = %s " % a)


# # 数据类型和变量的练习题
# n = 123
# f = 456.789
# print('n = %d' % n)
# print('f = %f' % f)
# print('Hello, world')
# print('Hello,\'Adam\'')
# print(r'Hello,"Bart"')
# s4 = r'''Hello,
# Lisa!'''
# print(s4)


# a = 'hello'*10
# print(a)


# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]

# # 打印Apple:
# print(L[0][0])
# # 打印Python:
# print(L[1][1])
# # 打印Lisa:
# print(L[2][2])


# # 条件判断练一练
# # age = input("请输入你的年龄:")


# # if int(age) >= 18:
# #     print("哥，已成年，网吧可以去了")

# # else:
# #     print("你还是一个小朋友哟，不能去网吧哟~~~")


# # height = input('请输入你的身高:(单位cm)')

# # if int(height) > 150:
# #     print("您需要买票哟~")

# # else:
# #     print("您还是小朋友，不需要买票哟~")


# # 乘坐公交车

# money = 1
# seat = 0

# if money > 2:
#     print("有车票，可以去找她了")
#     if seat == 1:
#         print("还有座位，可以坐下，美滋滋~~~")
#     else:
#         print("没有座位了，只能站着....")
# else:
#     print("没钱，找不了她了，呜呜呜....")


# # 猜拳游戏
# # i += 1
# # i = i + 1

# # 100的和
# # i = 2
# total = 0
# # while i <= 100:
# #     total = total + i
# #     i += 2
# # print(total)


# for i in range(101):
#     total = total + i

# print(total)

# # 打印1~100内，不能被7整除的所有数

# # i = 1
# # while i <= 100:
# #     if i % 7 == 0:
# #         i += 1
# #         continue

# #     else:
# #         print(i)
# #         i += 1
# # for i in range(101):
# #     if i % 7 == 0:
# #         continue
# #     else:
# #         print(i)


# # 乘法表
row = 1
uertical = 1
while row < 10:

    while uertical < row + 1:
        total = row * uertical
        print("%d*%d=%d\t" % (uertical, row, total), end="")
        uertical += 1
    print("\n")
    row += 1
    uertical = 1


# name = 'adbsf'
# print(name[0])

# mystr = "今天天气好晴朗，处处好风光呀好风光"
# print(mystr.find('好风光'))
# str = 'hello'
# print(str.ljust(10))


# def jiafa(a, b, c):
#     d = a + b
#     f = d - c
#     return d, f

# print(jiafa(1,2,3))


from turtle import st


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        a = 0
        total = high + 1 - low
        if total % 2 == 0:
            a = (total // 2)

        elif ((low % 2 != 0) & (high % 2 != 0)):
            a = (total // 2) + 1
        elif(low % 2 == 0) & (high % 2 == 0):
            a = (total // 2)

        return a

    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if ((x.count(x[0]) == 2) | (x.count(x[1] == 2)) | (x.count(x[2] == 2)) | (x.count(x[3] == 2))):
            return True
        else:
            return False

    def hammingWeight(self, n: int) -> int:
        n = str(n)
        print(n)
        total = n.count('1')
        return total


a = Solution
a.countOdds(a, low=3, high=7)
# a.isPalindrome(a,121)


def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

fact(1000)

