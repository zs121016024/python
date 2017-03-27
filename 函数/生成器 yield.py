#!/usr/bin/env python
# coding:utf-8

"""
带yield语句的函数称之为生成器函数，生成器函数的返回值是生成器

1.生成器函数执行的时候， 不会执行函数体
2.当next生成器的时候， 当前代码执行到之后的第一个yield, 会弹出值， 并且暂停函数
3.当再次next生成器的时候，从上一次展厅处往下执行
4.当没有多余的yield的时候，会抛出Stoplteration异常， 异常的value是函数的返回值

yield 是惰性求值，只有next生成器的时候才会调用yield

使用场景：
    一般用于计数器
"""

def g():
    for x in range(10):
        yield x   # 表示弹出一个值

r = g()   # 函数已经执行完成，函数的现场应该已经被销毁，但是实际上没有被销毁

print(next(r))  # 1
print(next(r))  # 2
print(next(r))  # 3

for x in r:
    print(x)






def gen():
    print('a')
    yield 1
    print('b')
    yield 2
    return 3
g = gen()

print(next(g)) # 执行第一个yield ，停止执行   输出 a 1
print(next(g)) # 执行第二个yield之后开始执行，在第二个yield的时候停止   输出 b 2
print(next(g)) # 从第二个yield开始执行，但没有更多的yield的时候，抛出StopIteration异常，异常的值正好是返回值  报异常 StopIteration: 3




#eg:用生成器写一个计数器，并且当输入三次的时候，就提示过期

def counter():
    x = 0
    while True:
        x += 1
        yield x
def inc(c):
    return next(c)

c = counter()

for _ in range(10):
    if inc(c) == 3:
        print('过期')
        break
    else:
        print(inc(c))



