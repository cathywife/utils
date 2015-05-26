#!/usr/bin/python
#-*- coding: utf-8 -*-


import functools


def log(arg):
    if callable(arg):
        # @log 模式
        func = arg
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print 'call %s():' % func.__name__
            return func(*args, **kw)
        return wrapper
    else:
        # @log('arg') 模式
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print '%s %s():' % (arg, func.__name__)
                return func(*args, **kw)
            return wrapper
        return decorator


@log('execute')
def now1():
    print '2013-12-25'


@log
def now2():
    print '2013-12-25'


if __name__ == "__main__":
    now1()
    now2()
