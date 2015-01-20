#!/usr/bin/python 
#-*- coding: utf-8 -*-


import os
import time
import signal


def fork(num):
    child_pid = os.fork()
    if child_pid == 0:   # 为0表示是子进程.
        print '子进程: %s' % os.getpid()
        while num > 1:
            print num
            num-=1
            time.sleep(1)
        #os._exit(0)   # 你可以在这里退出子进程.     
    else:    # 非0的时候返回子进程的进程号, 这部分是主进程.
        print '父进程: %s' % os.getpid()
        try:
           result = os.wait()    # 等待任何一个子进程结束.
           if result:
               print '子进程:', result[0], result[1]
           else:
               print '没有数据!'
        except:
           print '异常哦...'
    #  这部分的代码子程序和主进程都会执行.
    #os.exit(0)   # 你也可以在这里退出，注意，这里是父进程和子进程都共用的地方，在这里退出会导致父进程也一并退出.


if __name__ == "__main__":
    print fork(10)
