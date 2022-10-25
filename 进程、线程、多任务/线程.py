# 导入线程包
import threading
import time


def sing():
    for i in range(3):
        print("唱歌...")
        time.sleep(0.2)


def dance():
    for i in range(3):
        print("跳舞...")
        time.sleep(0.2)


if __name__ == '__main__':
    # 创建进程
    sing_thread = threading.Thread(target=sing, daemon=True)
    dance_thread = threading.Thread(target=dance)

    # 创建进程保护
    dance_thread.setDaemon(True)
    # 开启进程
    sing_thread.start()
    dance_thread.start()

    print("结束了...")
