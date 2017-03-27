#!/usr/bin/env python
# coding:utf-8

import time
import logging
import threading
import importlib
importlib.reload(logging)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s [%(threadName)s] %(message)s')

"""定时器、延迟执行"""
def worker():
    logging.info('running...')

t = threading.Timer(interval=5, function=worker) ###.Timer()方法，设置定时器，interval参数，设置延迟时间，function参数，设置函数

t.start()

#t.cancel()   ###当使用.cancel()方法后，interval设置无效，并且不会执行worker函数
             ###但是，当function参数所指定的函数开始执行的时候，.cancel()方法无效

