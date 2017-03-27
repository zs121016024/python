#!/usr/bin/env python
# coding:utf-8

"""
   多个线程运行时都需要去修改一个val的值，那么就对val添加一个锁，当前线程处理的时候，先锁上，等待处理完解锁，
   下一个线程继续锁上之后处理，之后再解锁
   这样能避免多个线程同时修改val的问题
"""

import logging
import threading
import random
import importlib
importlib.reload(logging)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s [%(threadName)s] %(message)s')


class Counter:
    def __init__(self):
        self.__val = 0
        self._lock = threading.Lock()  ###添加锁

    @property
    def value(self):
        with self._lock:    ###with语句的作用为，先执行acquire----执行-----release
                            ### 注意： 对于lock实例，只能调用一次acquire方法，再次调用会被阻塞，知道release被调用
            return self.__val

    def inc(self):
        with self._lock:
            self.__val += 1
    def dec(self):
        with self._lock:
            self.__val -= 1

counter = Counter()

def fn():
    if random.choice([-1, 1]) > 0:
        logging.info('inc')
        counter.inc()
    else:
        logging.info('dec')
        counter.dec()

for x in range(10):
    threading.Thread(target=fn).start()
print(counter.value)


