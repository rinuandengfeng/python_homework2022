'''
进程的使用
1. 导入multiprocessing
2. 创建子进程multiprocessing.Process(trageet = 函数名,args=元组，kwargs=字典)


'''

import multiprocessing
import os
import time


def sing(num):
    for i in range(num):
        print("唱歌...")
        # 查看子进程pid
        sing_pid = os.getpid()
        print("跳舞子进程pid:", sing_pid)
        # 查看父进程pid
        singf_pid = os.getppid()
        print("唱歌父进程pid:", singf_pid)
        time.sleep(0.5)


def dance(num):
    for i in range(num):
        print("跳舞...")
        # 查看子进程pid
        dance_pid = os.getpid()
        print("跳舞子进程pid:", dance_pid)
        # 查看父进程pid
        dancef_pid = os.getppid()
        print("跳舞父进程pid:", dancef_pid)
        time.sleep(0.5)


if __name__ == '__main__':
    # 创建进程
    # 使用args传递一个元组参数
    # 使用kwargs传递一个字典参数
    sing_process = multiprocessing.Process(target=sing, args=(3,))
    dance_process = multiprocessing.Process(target=dance, kwargs={"num": 3})
    # 开启唱歌进程守护
    sing_process.daemon = True
    # 开启跳舞进程守护
    dance_process.daemon = True
    # 启动唱歌进程
    sing_process.start()
    # 启动跳舞进程
    dance_process.start()

    # 查看进程id
    f = os.getpid()
    print("父进程pid:", f)
    time.sleep(1)

    print("进程结束了...")
