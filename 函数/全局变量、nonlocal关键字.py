#!/usr/bin/env python
# coding:utf-8

"""global"""
xx = 1
def fn():
    global xx   ### global可以提升变量作用域为全局变量，并且只对本作用域起作用，如果在其他作用域都需要生效，则需要在其他作用域也提升
    global yy   ### 不管有没有定义这个变量，global都可以提升为全局变量
    yy = 3
    xx += 1
print(fn())   ###打印出None
print(xx)     ### xx=2
print(yy)     ### yy=3




"""nonlocal关键字"""
def counter():
    x = 0
    def inc():
        nonlocal x   ### nonlocal关键字，用于标记一个变量由他的上级作用域定义，通过nonlocal标记的变量，可读可写
        x += 1
        return x
    return inc()
f = counter()
print(f)   # x = 1 ,在counter函数内，x= 0 ，用nonlocal标记之后，进行了 x += 1


def fn(x=[]):
    x.append(1)
    print(x)
print(fn())


def fn(lst=None):
    if lst is None:
        lst = []
    lst.append(3)   ### 如果传入的参数是非None ，则改变传入参数
    return lst
print(fn())


