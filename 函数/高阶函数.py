#!/usr/bin/env python
# coding:utf-8

"""
    返回函数或者参数是函数的函数 ---- 高阶函数
    因为python中函数是一等对象
    函数也是对象，并且它可以像普通对象一样赋值， 作为参数， 作为返回值
"""



"""
#装饰器
###定义outer函数的时候，把warapper函数重新定义成 function1/2/3，之后打印出来
# 通常情况下，我们定义函数的时候，为以下方式
# 现在新增加一个需求，需要在每个函数下面添加一个验证的输出，那么我们可以用装饰器
def function01():
    print('function01')

def function02():
    print('function02')

def function03():
    print('function03')

print(function01(), function02(), function03())


### 装饰器语法
def outer(function):    ###定义一个outer的函数，接收的参数为一个函数，返回也是一个函数
    def warapper():
        print('验证')
        function()      ###此处的function()函数和outer函数的参数 function 相对应
        print('取消')
    return warapper     ### outer函数内，返回一个为 warapper的函数

@outer    #python内的多糖语法，意思是在执行function01函数之前，先执行outer装饰器函数
def function01():
    print('function01')
@outer
def function02():
    print('function02')
@outer
def function03():
    print('function03')

print(function01(), function02(), function03())

#执行流程： outer函数---warapper函数---print验证---function函数---print取消


def outer(fn):
    def warapper(arg):   ### 装饰器内的函数 warapper带参数
        print('验证')
        fn(arg)
    return warapper
@outer
def function(arg):
    print('ok', arg)

print(function('zs'))
"""

"""装饰器
    参数是一个函数， 返回值是一个函数的函数
"""
import datetime

def logger(fn):   ### logger函数的参数为 fn，并且fn为一个函数
    def warp(*args, **kwargs):
        start = datetime.datetime.now()
        ret = fn(*args, **kwargs)   ###此处的fn函数与logger额fn参数一致
        end = datetime.datetime.now()
        print('call {} took {}'.format(fn.__name__, start - end))
        return ret   ### 对于warp函数，要return ret
    return warp     ### 对于logger函数， 要return warp， warp为一个函数

@logger
def add(x, y):
    return x + y

print(add(3, 5))

print(add.__name__)  ### 注意： 打印add的 __name__值的时候，值为warp，也就是装饰器上的函数名字




"""柯里化"""
import functools

import datetime

def logger(fn):
    @functools.wraps(fn)  ### 装饰器函数内部，添加functools.wraps()方法
    def wrap(*args, **kwargs):
        start = datetime.datetime.now()
        ret = fn(*args, **kwargs)
        end = datetime.datetime.now()
        print('call {} took {}'.format(fn.__name__, end - start))
        return ret
    return wrap

@logger
def add(x, y):
    return x + y

print(add(1, 2))
print(add.__name__)   ### 由于装饰器函数内部增加了 functools.wraps()方法，则add.__name__ 打印出的名字为函数本身名字



"""装饰器应用：
    1.针对一类问题做处理
    2.与具体业务逻辑无关
    3.常见的装饰器场景：
        监控、缓存、路由、权限、参数检查、审计等
"""