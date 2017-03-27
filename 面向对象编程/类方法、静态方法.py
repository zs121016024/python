#!/usr/bin/env python
# coding:utf-8

class I:
    def print(self):   # 无任何装饰， 这样的方法叫做实例方法
        return 'instance method'

    @classmethod # 当一个方法，被classmethod装饰的时候，这样的方法叫做类方法
    def class_print(cls):
        return 'class method'

    @staticmethod # 当一个方法，被staticmethod装饰的时候， 不会自动传入第一个参数， 这样的方法叫做静态方法
    def static_print():
        return 'static method'

i = I()
print(i.print())     #实例方法只能又实例调用


print(I.class_print())  #类方法可以被类调用，也能被实例调用,并且被实例使用时，传入的第一个参数还是类
print(i.class_print())

print(i.static_print())
print(I.static_print())

"""@property"""
#如下所示，修改成绩的一个小程序，判断set的值在0 到 100之间
class student:

    def get_source(self):
        return self._score
    def set_source(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = student()
s.set_source(60)  ###OK！
print(s.get_source())

#s.set_source(1000) ### 报错 ValueError: score must between 0 ~ 100!



class Student:

    @property # property 装饰器 会把一个仅有self参数的函数，变成一个属性，属性的值为方法的返回值
              # 此时，property又创建了一个 @score.setter的装饰器，负责把setter方法变成属性赋值
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 60
print(s.score)
s.score = 9999

