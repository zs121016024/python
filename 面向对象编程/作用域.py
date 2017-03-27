#!/usr/bin/env python
# coding:utf-8

class E:
    NAME = 'E' # 类的直接下级作用域， 叫做类变量

    def __init__(self, name):
        self.name = name

e = E('e')
print(E.NAME)

print(e.NAME)

print(e.name)

e2 = E('e2')
print(e2.NAME)
print(e2.name)

# python 可动态的给对象增减属性
# 当给实例的类变量赋值时， 相当于动态的给这个实例增加一个属性， 覆盖了类变量

#赋值即创建
def outer():
    v = 3
    def inner():
        v = 4

class E:
    NAME = 'E'

    def __init__(self, name):
        self.name = name
e = E('e')
print(e.NAME) # e.__class__.NAME

print(e.__class__.NAME)

e.__dict__['NAME'] = 'x'
print(e.NAME)  ### 输出 x

#属性查找顺序
#  __dict__ ------> __class__