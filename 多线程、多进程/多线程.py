#!/usr/bin/env python
# coding:utf-8

"""线程"""
import time
import threading    ###threading模块，用于Python处理线程
import logging      ###logging模块，相当于print输出
import importlib
importlib.reload(logging)   ###重新加载logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s [%(threadName)s] %(message)s')

def worker(num):
    logging.info('work-{}'.format(num))  ###输出信息

for x in range(3):   ###执行3个线程
    thread = threading.Thread(target=worker, args=(x, ), name='worker')   ###target 后面接函数名字，
                                                                            # args后传入参数，kwargs传入时候，应该用kwargs={'x':2}
                                                                            #name为标记线程名字
    thread.start()   ###.start()方法启动线程

"""daemon和non-daemon"""
def worker():
    logging.info('starting...')
    time.sleep(1)
    logging.info('completed...')
t = threading.Thread(target=worker, daemon=True)   ###daemon 默认为fasle
t.start()


"""获取所有线程"""
for t in threading.enumerate():
    logging.info(t.name)

"""实例化Thread类"""
class MyThread(threading.Thread):
    def run(self):
        logging.info('running')
t = MyThread()
t.start()     ###只有以继承的方式创建了线程，run方法和start方法才能同时使用
t.run()

t = threading.Thread(target=worker)
t.start()       ###不是以继承的方式创建的线程，run方法和start方法只能执行其中之一
#t.run()


"""thread local"""
ctx = threading.local()
ctx.data = 5
data = 'abc'
def worker():
    logging.info(data)
    logging.info(ctx.data)
worker()
#threading.Thread(target=worker).start()   ###thread local对象的属性， 只在当前线程可见





