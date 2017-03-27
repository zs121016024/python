#!/usr/bin/env python
# coding:utf-8

def add(x, y):
    return x + y ### return语句除了返回值之外，还会结束函数，return后面的将不会执行
    print('x + y')



def guess(x):   ### 一个函数可以有多个return,执行那个return ,则由那个return之后的代码返回内容，并结束函数
    if x > 3:
        return '> 3'
    return '<= 3'



def fn(x):
    for i in range(x):
        if i > 3:
            return i  ### 函数中， return 可以提前结束循环
        else:
            print('not bigger than 3')



def fn():  ###当函数没有return语句的时候，则返回None
    pass



def fn():  ###当需要返回多个值时，可以用封装把return的值返回成一个元组
    return 3, 5
print(fn())
x, y = fn()  ###可以通过解构获取多个返回值
print(x, y)



def fn():   ### return None 可以简写成 return ，通常用于结束函数
    return
