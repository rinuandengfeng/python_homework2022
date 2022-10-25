'''
好友管理系统，实现添加好友、删除好友、备注好友、展示好友
'''

friend = []
print("1.添加好友")
print("2.删除好友")
print("3.备注好友")
print("4.展示好友")

try:
    while True:
        num = int(input("请输入序号:"))
        if num == 1:
            add_name = str(input("请输入添加的好友:"))
            friend.append(add_name)
            print("添加好友成功！")
        elif num == 2:
            del_name = str(input("请输入删除的好友名:"))
            if del_name in friend:
                friend.remove(del_name)
                print("删除好友成功！")
            else:
                print("输入错误，您没有改好友o(╥﹏╥)o")
        elif num == 3:
            b_name = str(input("请输入要修改的好友名:"))
            a_name = str(input("请输入修改后的好友名:"))
            name_index = friend.index(b_name)
            friend[name_index] = a_name
            print("备注成功！")
        elif num == 4:
            print("好友列表为:")
            for i in friend:
                print(i)
        else:
            print('输入错误，退出系统')
            break
except:
    print("输入错误，请重新登录~")
