'''
模拟登录
'''
# 定义用户名
uname = 'admin'
# 定义密码
passwd = '123'
# 接收用户输入的用户名
username = input('请输入用户名:')
password = input('请输入密码:')
n = 1
while n < 5:
    if username == uname and password == passwd:
        print("登录成功")
        break
    elif username != uname or password != passwd:
        if (3-n) > 0:
            print("您还有{}次机会".format(3 - n))
            username = input('请输入用户名:')
            password = input('请输入密码:')
        else:
            print("输入错误次数过多，请稍后再试╮(╯▽╰)╭")
            break
        n += 1


