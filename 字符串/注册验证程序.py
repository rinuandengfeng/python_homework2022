user_name = input("请输入用户名（以_开头，3-30个字符）：")
password = input("请输入密码（由下划线、数字和字母共同组成，8-16个字符）：")
if user_name[0] != '_' :
    print("用户名请使用下划线开头")
elif 3 > len(user_name) or 30 < len(user_name):
    print("用户名长度不符合规定")
elif 8 > len(password) or 16 < len(password):
    print("密码长度不符合规定")
elif password.find('_') == -1 :
    print("密码中未输入下划线")
else:
    passwords = password.replace('_' , '1')
    if passwords.isalnum():
        print("恭喜你，注册成功！用户名：",user_name,"密码：",password)
    else:
        print("密码中有其他符号，注册失败!")