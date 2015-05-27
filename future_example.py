#!/usr/bin/python
#-*- coding: utf-8 -*-


""" __future__ 示例, 此脚本执行环境是 Python2.

Python3 和 Python2 字符串比较:  
在 2.x 里的字符串用'xxx'表示str, Unicode字符串用u'xxx'表示unicode; 
在 3.x中, 所有字符串都被视为unicode, 写u'xxx'和'xxx'是完全一致的.

import unicode_literals 时候结果是:
'xxx' is unicode? True
u'xxx' is unicode? True
'xxx' is str? False
b'xxx' is str? True

不 import unicode_literals 的时候结果是:
'xxx' is unicode? False
u'xxx' is unicode? True
'xxx' is str? True
b'xxx' is str? True


再看下除法, import division 的时候结果是:
10 / 3 = 3.33333333333
10.0 / 3 = 3.33333333333
10 // 3 = 3

不 import division 的时候结果是:
10 / 3 = 3
10.0 / 3 = 3.33333333333
10 // 3 = 3


另外, from __future__ import absolute_import 可以强制使用绝对引用, 
禁止隐士相对引用, 从 Python3 开始默认强制使用绝对引用(Python2.7 
可能禁止).


from __future__ import with_statement 这条语句可以安全的关闭使用 with
 打开的句柄等资源(从 Python2.6 开始已经支持此选项, 不用 import).


from __future__ import print_function 这条语句是把 print 变成一个函数,
从 Python3 开始强制使用 print 函数, print '' 这种语句会报错. 

"""

from __future__ import unicode_literals, division


print '\'xxx\' is unicode?', isinstance('xxx', unicode)
print 'u\'xxx\' is unicode?', isinstance(u'xxx', unicode)
print '\'xxx\' is str?', isinstance('xxx', str)
print 'b\'xxx\' is str?', isinstance(b'xxx', str)


print '10 / 3 =', 10 / 3
print '10.0 / 3 =', 10.0 / 3
print '10 // 3 =', 10 // 3

