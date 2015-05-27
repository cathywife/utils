#!/bin/env python
#-*- coding: utf-8 -*-

""" 时间相比的例子, 要在 Python2.7 以上运行.

"""

import datetime


def main():
    _time  = "201502051500"
    sub  = datetime.datetime.now() - datetime.datetime.strptime(_time, '%Y%m%d%H%M')
    print sub.total_seconds()


if __name__ == "__main__":
    main()
