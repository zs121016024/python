#!/usr/bin/env python
# coding:utf-8

"""
类的继承
"""

class Base:   ###父类（基类）
    def base_print(self):
        return 'base'
class A(Base):   ###继承Base类
    def a_print(self):
        return 'a'

a = A()
print(a.a_print())   ### 调用自身的方法

print(a.base_print())  ### 调用父类的方法

###注意：
#   凡是共有的都能继承
#   凡是私有的都不能继承
#   原来是什么， 继承过来还是什么



"""
    方法重写
"""

class Base:
    def __init__(self):
        self.__a = 4

    def print(self):
        return 'Base.print'

    @classmethod
    def cls_print(cls):
        return 'Base.cls_print'

class Sub(Base):
    def print(self): ###当子类和父类有同名成员的时候，子类的成员会覆盖父类的同名成员
        return 'Sub.print'

class SubSub(Sub):
    def print(self):
        return 'SubSub.print'

    @classmethod
    def cls_print(cls):
        return 'SubSub.cls_print'

    def foo(self):
        super(SubSub, self).print()
        super(Sub, self).print()
        super(SubSub, SubSub).cls_print()

    @classmethod
    def cls_foo(cls):
        super(Sub, cls).cls_print()



sub = Sub()
print(sub.print())



