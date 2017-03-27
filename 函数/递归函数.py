#!/usr/bin/env python
# coding:utf-8

"""
什么是递归：
    递归就是函数体内，调用自身
递归特性：
    1.必须有一个明确的结束条件
    2.每次进入更深一层递归时，问题规模相比上次递归都应有所减少
    3.递归效率不高，递归层次过多，会导致栈溢出
注意：
    函数不能像 while那样一直循环下去，函数递归最大只能递归999次
"""

#菲波那切数列  递归演示
# fib(n) = 1 if n = 0
# fib(n) = 1 if n = 1
# fib(n) = fin(n-1) + fib(n-2)

def fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(4))



#打印100以内的奇数，以递归来实现
def fun(n):
    "打印100以内的奇数"
    if n <= 100:
        print(n)
        n += 2
        return fun(n)
fun(1)
