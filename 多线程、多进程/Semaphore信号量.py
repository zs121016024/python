#!/usr/bin/env python
# coding:utf-8

"""
信号量
"""

import logging
import threading
import random
import datetime
import importlib
importlib.reload(logging)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s [%(threadName)s] %(message)s')
