#!/usr/bin/env python
# coding:utf-8
"""
queue   队列---先进先出
        可以实现暂存
        无法实现广播
        通常情况下，queue 和 condition同时使用，用condition实现广播

        queue.Queue是线程安全的，不用加锁能实现正确并发

        全局解释器锁，GIL

        内置容器都是线程安全的
"""

import queue
q = queue.Queue(maxsize=5)   ###maxsize 最大长度
q.put()

queue.Queue 方法，实现先进先出
queue.PriorityQueue 优先队列