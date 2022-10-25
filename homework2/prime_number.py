"""
判断输入的数是不是素数
"""
n = int(input("请输入一个正整数(n >= 2):"))
if n >= 2:
    for i in range(2, n):
        # 只要有一个能够整除就不是素数
        if n % i == 0:
            print("{}不是素数!".format(n))
            break

    else:
        print("{}是素数".format(n))
else:
    print("不好意思哟，您输入错误了(ㄒoㄒ)~~")
