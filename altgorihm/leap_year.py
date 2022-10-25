# year = int(input("请输入年份:"))
#
#
#
# #判断是否为闰年
# if (year % 4 == 0 and year % 100 != 0 ) or (year % 400 == 0):
#     #是闰年打印L
#     print("Yes")
# else:
#     #不是闰年打印N
#     print("No")
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

try:
    for i in sys.stdin:
        year = int(i)
        # 判断是否为闰年
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            # 是闰年打印L
            print("Yes")
        else:
            # 不是闰年打印N
            print("No")
except:
    print("输入错误")
