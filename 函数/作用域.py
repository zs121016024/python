#!/usr/bin/env python
# coding:utf-8

"""作用域
    作用域是一个变量的可见范围叫做这个变量的作用域
"""

x = 1   # x 定义在全局作用域中
def inc():  # 函数内部是一个局部作用域，不能直接用于全局作用域的变量
    return x
print(inc())


def fn(): #上级作用域对下级作用域是只读可见
    xx = 1
    print(xx)
    def inner():
        xx = 2  # 赋值即定义，  在下级作用域里面， 重新定义了 xx
    inner()
print(fn())
#不同作用域变量不可见，但是下级作用域对上级作用域的变量只读可写








