#!/usr/bin/env python
# coding:utf-8
"""
使用场景：
1、10个工作，当全部完成，才执行后面的程序
2、10个工作，只需要设定一个阀值，当完成了当前阀值相当的工作，才执行后面的程序
"""
import threading
import logging
import importlib
import time
importlib.reload(logging)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s [%(threadName)s] %(message)s')

def worker(barrier: threading.Barrier):
    logging.info('waitting for {} threads'.format(barrier.n_waiting))
    try:
        worker_id = barrier.wait()
        logging.info('after barrier {}'.format(worker_id))
    except threading.BrokenBarrierError:
        logging.warning('aborting')

barrier = threading.Barrier(3)

for x in range(3):
    threading.Thread(target=worker, name='work-{}'.format(x), args=(barrier, )).start()
    time.sleep(0.5)
logging.info('started')


barrier = threading.Barrier(3)   ###threading.Barrier(3) 当有3个线程都完成之后（阀值），才进入下一个程序

def abort(barrier):
    logging.info('aborting')
    barrier.abort

for x in range(2):
    threading.Thread(target=worker, name='worker-{}'.format(x), args=(barrier, )).start()

barrier.abort()  ###当abort方法被执行的时候， wait方法会抛出BrokenBarrierError异常