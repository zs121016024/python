#!/usr/bin/env python
# coding:utf-8

"""
    匿名函数 lambda
    1.用lambda来定义
    2.参数列表不需要用小括号
    3.冒号不是用来开启新语句块
    4.没有return， 最后一个表达式的值即返回值
"""

la = (lambda x: x+1)(3)
print(la)

f = lambda x: x + 1
print(f(5))

num = (lambda x, y=3: x+y)(5)
print(num)

num = (lambda *args: args)(*range(3))
print(num)

num = (lambda *args, **kwargs: print(args, kwargs))(*range(3), **{str(x): x for x in range(3)})
print(num)






