#!/usr/bin/env python
# coding:utf-8

"""
import socketserver


class EchoHandler(socketserver.BaseRequestHandler):
    def setup(self):
        # 初始化工作 通常情况下不需要重写
        print('setup {}:{}'.format(*self.request.getpeername()))
        super().setup()

    def finish(self):
        # 清理工作 通常情况下也不需要重写
        print('finish {}:{}'.format(*self.request.getpeername()))
        super().finish()

    def handle(self):

        conn = self.request
        conn.send('hello'.encode())
        flage = True
        while flage:
            message = self.request.recv(1024).strip()
            print(message)

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8888), EchoHandler)
    try:
        server.serve_forever()  # 启动server
    except KeyboardInterrupt:
        server.shutdown()
        server.server_close()  # 关闭


"""
#IO多路复用

#!/usr/bin/env python
# coding:utf-8

"""
概念

同步、异步
    发生在函数、方法调用的时候，是否得到直接的最终结果，得到直接的最终结果是同步，反之为异步

阻塞与非阻塞
    发生在函数、方法调用的时候， 是否立刻返回， 立刻返回是非阻塞， 反之为阻塞

    同步、异步和阻塞、非阻塞在概念上是不相关的
    区别在于：
        同步、异步关注的是 "结果"
        阻塞、非阻塞关注的是 "是否等待"

同步IO/异步IO/IO多路复用
    发生在IO的时候：
        1、内核从输入设备读写数据
        2、进程从内核复制数据
    同步IO:
        阻塞IO: 进程等待，直到读写完成   read/writ
        非阻塞IO： 进程不等待， 如果IO设备没有准备好， 返回error。 内核和用户空间之间复制数据是阻塞的    read/writ
        IO多路复用： 阻塞的，直到其中一个IO设备准备好   select/poll/epoll/kqueue/iocp
    异步IO:
        进程发起IO请求，内核完成IO的两步，然后通知进程

"""

#DefaultSelect会根据平台，选择其中性能最高的一个
#SelectSelect   实现select
#PollSecect      实现poll
#EpollSelect     实现epoll

import selectors
import socket
import threading
"""
selector = selectors.DefaultSelector()

def read(conn):
    message = conn.recv(1024).strip()
    print('recv {}\r\n'.format(message.decode()))
    conn.send(message)

def accept(sock):
    conn, _ = socket.accept()
    conn.setblocking(False)
    selector.register(conn, selectors.EVENT_READ, read)

socket = socket.socket()   #初始化
socket.bind(('127.0.0.1', 8888))  #bind
socket.listen(50)  #listen

key = selector.register(socket, selectors.EVENT_READ, accept)#注册一个处理函数，当sock读准备好的时候，调用这个函数    selectors.EVENT_READ 准备读
                                                        #IO多路复用基于事件的，对于IO来说有哪些事件， 1.读准备好（内核准备输入输出设备）
                                                                                              #2.写准备好
                                                            #返回的是一个selectorkey的对象
event = threading.Event()
try:
    while not event.is_set():
        events = selector.select(1)
        for key, _ in events:
            key.data(key.fileobj)
except KeyboardInterrupt:
    event.set()
    socket.close()
    selector.unregister(socket)
"""


#实例

from queue import Queue

from collections import namedtuple
Client = namedtuple('Client', ['conn', 'queue', 'handler'])

class ChartServer:
    def __init__(self, host='127.0.0.1', port=8000):
        self.host = host
        self.port = port
        self.sock = socket.socket()
        self.selector = selectors.DefaultSelector()
        self.clients = {}

    def handle(self, conn, mask):
        pass

    def accept(self):
        conn, client_address = self.sock.accept()
        self.clients[client_address] = Client(conn, Queue(), )
    def start(self):
        self.socket.bind(self.host, self.port)
        self.sock.listen()
        self.selector.register(self.sock, selectors.EVENT_READ, self.handle)
        self.selector.register()

