'''
模拟登录系统
'''
users = ['root', 'westos', 'zhangsan', 'admin']
passwd = ['123', '456', '789', '999']
i = 1
while i < 4:
    username = input("请输入账户名:")
    password = input("请输入密码:")
    if username in users:
        username_index = users.index(username)
        if password == passwd[username_index]:
            print("登录成功！")
            break
        else:
            print("用户名或密码输入错误，请重新登录。")
            i += 1
    else:
        print('用户名输入错误，请重新登录。')
        i += 1
