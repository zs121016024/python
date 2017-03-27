#!/usr/bin/env python
# coding:utf-8

"""函数基础"""

"""定义函数"""
def function(x, y):   ### x , y 为函数带的参数
    return x + y      ###return 语句，调用函数时，return方式返回函数的值

"""调用函数"""
fun = function(1, 2)  ###1， 2 为调用函数时，传入参数的值
fn = function(x=1, y=2)  ###传入参数时，可以用"参数名字"="值"的方式传入
print(fun)
print(fn)



"""参数默认值"""
def inc(base, x=1):   ###x = 1为参数的默认值，base为需要传入的值,注意：传入参数时，默认为从左往右依次传入，需要注意顺序
    return base + x
print(inc(1))

def connect(host='127.0.0.1', port=3306, user='root', password='', db='test'):
    pass

connect('172.1.1.1',password='123456')

"""可变参数"""
def sum(*args):  ###参数前加一个*号，表示这个参数是可变的，也就是说可以接受任意多个参数，
                 # 这些参数将构成一个元组，此时只能通过为止参数传参
    print(type(args))
    ret = 0
    for x in args:
        ret += x
    return ret
print(sum(1, 2, 3))


def connect(**kwargs):
    print(type(kwargs))
    for k, v in kwargs.items():
        print('{} => {}'.format(k, v))

print(connect(host='127.0.0.1', port=3306))

#####注意：
#####    可变参数两种形式：
#        1.位置可变参数： 参数名前加一个*号，构成元组，传参只能以位置参数形式
#        2.关键字参数：   参数名前加两个*号，构成字典，传参只能以关键字参数形式

def fn(*args, **kwargs):  ###位置可变参数可以和关键字参数一起使用，但是位置参数必须在前面
    print(args)
    print(kwargs)

print(fn(1, 2, 3, 4, a=1, b=2))


def fn(x, y, *args, **kwargs):    ###普通参数可以和可变参数一起使用，但是传参的时候必须匹配
    print(x)
    print(y)
    print(args)
    print(kwargs)
print(fn(1, 2, 3, 4, 5, a=1, b=2))


def fn(x=5, *args):    ###关键字可变参数不允许在普通参数之前
    print(x)
    print(args)

print(fn(1, 2, 3, 4, 5))


###总结：
    #1.默认参数靠后
    #2.可变参数靠后
    #3.默认参数和可变参数不同时出现



"""参数解构"""
def add(x, y):
    ret = x + y
    print('{} + {} = {}'.format(x, y, ret))
    return ret
print(add(1, 2))






