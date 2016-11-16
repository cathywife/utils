#!/usr/bin/env python
# -*- coding: utf-8 -*-


import subprocess


def pipeline(cmd):
    """ 执行命令, 循环输出执行结果 """
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    while proc.poll() is None:
        line = proc.stdout.readline()
        if not line: continue
        print line[:-1]


if __name__ == "__main__":
    cmd = "echo 1; sleep 1 ;echo 2"
    pipeline(cmd)
