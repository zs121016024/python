#!/usr/bin/env python
# coding:utf-8

class A:
    def __init__(self, a, b, c, d):
        print(a)
        print(b)
        print(c)
        print(d)
a = A(1, 2, 3, 4)
print(a)

#创建对象使用类名(__init__ 函数除第一个参数外的参数列表)
#创建对象的时候 实际执行了 __init__ 函数
#__init__ 函数并不会创建对象
#__init__函数初始化对象

#首先创建对象
#对象作为self参数传递给 __init__函数
#返回self

class Door:
    def __init__(self, number, status):
        self.number = number
        self.status = status

    def open(self): #方法
        self.status = 'opening'

    def close(self):
        self.status = 'closed'
door = Door(1001, 'closed')  #实例化类
print('The door is {}'.format(door.status))

Door.open(door)
print('The door is {}'.format(door.status))



