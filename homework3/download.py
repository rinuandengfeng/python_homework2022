'''
在互联网上下载文件时，经常会跳出一个提示窗口，询问用户是否执行下载命令，此时若用户选择“y”或“Y”便会执行下载任务，若选择“n”或“N”便会退出下载任务。
'''
# 接收输入的值
values = input('是否确定下载?请输入Y/y或N/n')
# 判断是否是输入的'Y'或'y'
if values == 'Y' or values == 'y':
    print("正在下载中……")
# 判断是否是输入的'N'或'n'
elif values == 'N' or values == 'n':
    print("正在取消下载……")
