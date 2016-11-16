#-*- coding: utf-8 -*-


import os
import subprocess
import re
import random
import time


def shell(cmd):
    process = subprocess.Popen(
        args=cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    std_out, std_err = process.communicate()
    return_code = process.poll()
    return return_code, std_out, std_err


def rand_passwd():
    """ 随机生成密码.

    """
    total_len = 30
    base_str1 = ['!', '@', '#', '=', '-', '_', '+']
    base_str2 = [str(i) for i in range(0, 10)]
    base_str3 = [chr(i)
                 for i in range(ord('A'), ord('Z') + 1) + range(ord('a'), ord('z') + 1)]
    random.seed()
    total_sample = []
    total_sample += random.sample(base_str1, random.randint(1, len(base_str1)))
    total_sample += random.sample(base_str2, random.randint(1, len(base_str2)))
    total_sample += random.sample(base_str3, total_len - len(total_sample))
    random.shuffle(total_sample)
    passwd = ''.join(total_sample)
    return passwd


def mac_random():
    mac = [0x00, 0x16, 0x3e, random.randint(0x00, 0x7f),
           random.randint(0x00, 0xff), random.randint(0x00, 0xff)]
    s = []
    for item in mac:
        s.append(str("%02x" % item))

    return ':'.join(s)


def check_wait(check_cmd, post_cmd, timeinit=0, interval=10, timeout=600):
    """ 循环等待某一条件成功,就执行 post_cmd,时间超过 timeout 就超时.

    """
    timetotal = timeinit

    while timetotal < timeout:
        rc, ro, re = shell(check_cmd)
        if rc == 0:
            rc, ro, re = shell(post_cmd)
            if rc == 0:
                return True
            else:
                return False

        time.sleep(interval)
        timetotal += interval

    return False


def check_wait_null(check_cmd, timeinit=0, interval=10, timeout=600):
    """ 循环等待某一条件成功,返回 True, 时间超过 timeout 就超时.
    用到了 shell 函数.

    """
    timetotal = timeinit

    while timetotal < timeout:
        rc, ro, re = shell(check_cmd)
        if rc == 0:
            return True

        time.sleep(interval)
        timetotal += interval

    return False
