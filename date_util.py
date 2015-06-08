#!/bin/env python
#-*- coding: utf-8 -*-

""" 时间的几个例子. 

1. 时间相比的例子, 要在 Python2.7 以上运行.

2. 根据时间字符串生成绝对时间数字. 

备忘一下时间格式:
    Directive   Meaning Notes
    %a  Locale’s abbreviated weekday name.
    %A  Locale’s full weekday name.
    %b  Locale’s abbreviated month name.
    %B  Locale’s full month name.
    %c  Locale’s appropriate date and time representation.
    %d  Day of the month as a decimal number [01,31].
    %H  Hour (24-hour clock) as a decimal number [00,23].
    %I  Hour (12-hour clock) as a decimal number [01,12].
    %j  Day of the year as a decimal number [001,366].
    %m  Month as a decimal number [01,12].
    %M  Minute as a decimal number [00,59].
    %p  Locale’s equivalent of either AM or PM. (1)
    %S  Second as a decimal number [00,61].     (2)
    %U  Week number of the year (Sunday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Sunday are considered to be in week 0.    (3)
    %w  Weekday as a decimal number [0(Sunday),6].
    %W  Week number of the year (Monday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Monday are considered to be in week 0.    (3)
    %x  Locale’s appropriate date representation.
    %X  Locale’s appropriate time representation.
    %y  Year without century as a decimal number [00,99].
    %Y  Year with century as a decimal number.
    %Z  Time zone name (no characters if no time zone exists).
    %%  A literal '%' character.

"""

import datetime
import time


def date_diff():
    _time  = "201502051500"
    sub  = datetime.datetime.now() - datetime.datetime.strptime(_time, '%Y%m%d%H%M')
    return sub.total_seconds()


def get_time_from_string(string="Mon Jun 8 13:35:02 2015"):
    time_struct = time.strptime(string, "%a %b %d %H:%M:%S %Y")
    return time.mktime(time_struct)


if __name__ == "__main__":
    print date_diff()
    print get_time_from_string()
