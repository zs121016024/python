#!/usr/bin/env python
# coding:utf-8

"""
生产者消费者模型 Condition
生产者生产消息后，使用notify或者notify_all通知消费者进行消费
消费者使用wait方法阻塞等待生产者通知
notify通知指定个wait的线程，notify_all通知所有的wait线程
无论notify/notify_all/wait都必须先acqurie，完成后必须确保release, 通常使用with语法
"""

import threading
import logging
import random
import importlib
importlib.reload(logging)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s [%(threadName)s] %(message)s')


class Dispatcher:
    def __init__(self):
        self.data = None
        self.event = threading.Event()
        self.cond = threading.Condition()

    ###消费者
    def consumer(self):
        while not self.event.is_set():
            with self.cond:
                self.cond.wait()  ###等待notify通知
                logging.info(self.data)

    ###生产者
    def producer(self):
        for _ in range(10):
            data = random.randint(0, 100)
            logging.info(data)
            self.data = data
            with self.cond:
                self.cond.notify()  ###通知consumer可以进行处理
            self.event.wait(1)   ###每一秒产生一条消息
        self.event.set()  ###consumer 遇到.set()方法，退出

d = Dispatcher()  ###初始化类

p = threading.Thread(target=d.producer, name='producer')  ###开始生产消息，名字为producer

for x in range(4):
    threading.Thread(target=d.consumer, name='consumer-{}'.format(x)).start()

p.start()