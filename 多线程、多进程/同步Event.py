#!/usr/bin/env python
# coding:utf-8

"""
threading.Event()

wait会阻塞线程，知道set方法被调用或者超时
event 可以再线程之间发送信号
通常用于某个线程需要等待其他线程处理完成某些动作之后才能启动

通俗来讲，wait是设置没隔多长时间执行一次程序，并且是一直执行，set是当程序通过wait执行之后，遇到set时果断放弃当前执行程序并退出
当wait没有遇到set方法的时候会一直执行下去

"""

import logging
import threading
import random
import datetime
import importlib
importlib.reload(logging)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s [%(threadName)s] %(message)s')

def worker(event: threading.Event):
    s = random.randint(1, 5)
    event.wait(s)
    event.set()
    logging.info('sleep {}'.format(s))

def boss(event: threading.Event):
    start = datetime.datetime.now()
    event.wait()
    logging.info('worker exit {}'.format(datetime.datetime.now() - start))

def start():
    event = threading.Event()
    b = threading.Thread(target=boss, args=(event, ), name='boss')
    b.start()
    for x in range(5):
        threading.Thread(target=worker, args=(event, ), name='worker-{}'.format(x)).start()
start()





