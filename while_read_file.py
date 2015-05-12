#!/bin/env python
# -*- coding: utf-8 -*-


def _funtion(str):
    return str


def while_read_file(file_path):
    with open(file_path, 'rb') as f:
        # 从行尾前十个字符开始读.
        # 0 表示从行首;
        # 1 表示当前位置.
        f.seek(-10, 2) 
        while 1:
            str = f.readline().strip()
            if str:
                _funtion(str)


if __name__ == "__main__":
    while_read_file("/tmp/test")

