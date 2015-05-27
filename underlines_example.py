#!/usr/bin/python
# -*- coding: utf-8 -*-

""" 演示 _method, __method 和 __method__ 的区别.

_method 表示私有函数, 只能从内部调用(强制显示调用也可以, 
但是不推荐这么做);
 
__method 表示它是一个不可覆盖的函数, 比如A类声明了__method
, B类继承A, 即使B类也声明了__method, __method 还是A的
__method, B类的声明无效, 因为如果类一个声明了__method, 
Python会把它改成 _类名__method, 所以继承的类也修改不了, 
__method 不常用;

对于__method__, 它是操作符或者是被称为魔法函数的本地函数, 
你不必调用它, Python 来调用它, 类似的函数有 __init__, __new__
和 __this__ 等. 看下面:

In [178]: name = "igor"

In [179]: name.__len__()
Out[179]: 4

In [180]: len(name)
Out[180]: 4

In [181]: number = 10

In [182]: number.__add__(20)
Out[182]: 30

In [183]: number + 20
Out[183]: 30

"""


# 看一下 __method.
class A(object): 
    def __method(self):
        print "I'm a method in A" 

    def method(self): 
        self.__method() 

a = A() 
a.method()
# 可以看到 _A__method 这个方法, 说明Python 把__method改成了
# _A__method, 所以B修改不了.
print A.__dict__.keys()
a._A__method()   # 最好不用这么用.

class B(A): 
    def __method(self): 
        print "I'm a method in B" 

b = B() 
b.method()
# 可以看到B也有_B__method方法.
print B.__dict__.keys()
b._B__method()   # 最好不要这么用.


# __method__ 的例子, 这个例子重载了运算符.
class CrazyNumber(object):

    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return self.n - other

    def __sub__(self, other):
        return self.n + other

    def __str__(self):
        return str(self.n)

num = CrazyNumber(10)
print num           
print num + 5       
print num - 20      
print isinstance(str(num), str)

# __method__ 另一个例子.
class Room(object):

    def __init__(self):
        self.people = []

    def add(self, person):
        self.people.append(person)

    def __len__(self):
        return len(self.people)

room = Room()
room.add("Igor")
print room.__len__()   # 显示调用也可以, 但不用这么用.
print len(room)   # 如果没有__len__函数, 会报错. 
