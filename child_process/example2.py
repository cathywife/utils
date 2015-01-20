#!/usr/bin/python 
#-*- coding: utf-8 -*-


import os
import time
import signal


def fork(num):
    child_pid = os.fork()
    if child_pid == 0:
        print '子进程: %s' % os.getpid()
        while 1:    # 死循环.
            print num
            time.sleep(1)
    else:
        def _exit(signal_num, frame):
            os.kill(child_pid, signal_num)   # 子进程退出.
            os._exit(os.getpid())    # 主进程退出.
        signal.signal(signal.SIGTERM, _exit)   # 发现如果用 os.wait() 等待子程序技术, 则接收不了信号.

        print '父进程: %s' % os.getpid()
        time.sleep(100)   # 接收到 TERM 信号后, 此句被中断.


if __name__ == "__main__":
    print fork(10)
