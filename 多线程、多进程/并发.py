#!/usr/bin/env python
# coding:utf-8
"""
#线程
import threading    ###导入threading模块

def worker():       ###定义worker函数
    print('work..')

thread = threading.Thread(target=worker)  ###调用threading.Thread方法，target后面是需要调用的函数

thread.start()    ###.star()方式为执行，当这个线程的逻辑执行完毕的时候，线程会自动退出，Python没有提供主动退出的方法
"""


"""
import time
import threading
def worker(num):
    time.sleep(1)
    print('work-{}'.format(num))

for x in range(5):
    t = threading.Thread(target=worker, args=(x, ))
    t.start()
"""

"""
###logging
import logging
import threading
import importlib

importlib.reload(logging)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s [%(threadName)s] %(message)s')
logging.warning('警告!!!')   ###logging.warning（）方法，可用作警告信息

logging.error('错误!!!')     ###logging.error()方法，可用作错误信息

def worker(num):
    logging.warning('work-{}'.format(num))    ###用logging代替print

for x in range(5):
    t = threading.Thread(target=worker, args=(x, ))
    t.start()
"""



"""
###参数
import logging
import importlib
import threading
import time
importlib.reload(logging)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s [%(threadName)s] %(message)s')

def add(x, y):
    logging.info(x + y)

add(1, 2)

add(x=1, y=2)

threading.Thread(target=add, args=(1, 2)).start()

threading.Thread(target=add, kwargs={'x':1, 'y':2}).start()

threading.Thread(target=add, args=(1, ), kwargs={'y':2}).start()
"""


"""
import logging
import importlib
import threading
import time
importlib.reload(logging)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s [%(threadName)s] %(message)s')

###控制线程名字

threading.Thread(target=add, args=(1, 2), name='add').start() ###name后接线程名字

def work():
    logging.info('starting')
    time.sleep(2)
    logging.info('completed')

t1 = threading.Thread(target=work, name='worker')  ###线程名字可以重名，线程名不是线程的唯一标识，但是通常都应该避免
t2 = threading.Thread(target=work, name='worker')

t1.start()
t2.start()
"""


"""
#daemon 与 non-daemon
import logging
import importlib
import threading
import time
importlib.reload(logging)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s [%(threadName)s] %(message)s')

def work():
    logging.info('starting')
    time.sleep(2)
    logging.info('completed')

t = threading.Thread(target=work, daemon=True)
t1 = threading.Thread(target=work)


class MyThread(threading.Thread):
    def run(self):
        logging.info('run')

# t = MyThread()
# t.start()
#
# t.run()

t = threading.Thread(target=work)
t.run()
t.start()

"""


