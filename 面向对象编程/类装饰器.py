#!/usr/bin/env python
# coding:utf-8

"""
类装饰器
参数传入一个类，返回一个类
"""

def set_name(name):
    def warp(cls):  ###参数传入类
        cls.NAME = name
        return cls ### 返回cls类
    return warp

@set_name('G')
class G:
    pass

print(G.NAME)








def print_name(cls):
    def get_name(self):
        return cls.__name__
    cls.__get_name__ = get_name
    return cls

@print_name
class H:
    pass

h = H()
print(h.__get_name__())


###类装饰器通常用于给类增加属性，方法都是类级