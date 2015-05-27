#!/usr/bin/python
#-*- coding: utf-8 -*-


""" __future__ 示例, 此脚本执行环境是 Python2.

Python3 和 Python2 字符串比较:  
在 2.x 里的字符串用'xxx'表示str, Unicode字符串用u'xxx'表示unicode; 
在 3.x中, 所有字符串都被视为unicoder, 写u'xxx'和'xxx'是完全一致的.

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

"""

from __future__ import unicode_literals, division


print '\'xxx\' is unicode?', isinstance('xxx', unicode)
print 'u\'xxx\' is unicode?', isinstance(u'xxx', unicode)
print '\'xxx\' is str?', isinstance('xxx', str)
print 'b\'xxx\' is str?', isinstance(b'xxx', str)


print '10 / 3 =', 10 / 3
print '10.0 / 3 =', 10.0 / 3
print '10 // 3 =', 10 // 3

