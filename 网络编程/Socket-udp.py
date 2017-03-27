#!/usr/bin/env python
# coding:utf-8

"""
    udp server 不需要也不能执行listen
    udp server 不需要也不能执行 accept

    只需要两步：
    1.初始化(注意type参数)
    2.bind

    使用resvfrom(1024)  接收数据
    只能以sendto(b'hello\n', ('127.0.0.1', 1001))    发送数据

    udp是无连接的，可以随时close()无任何问题
"""

"""
问答小程序：
#server：
import socket

ip_port = ('127.0.0.1', 8888)                   #定义IP, 端口
s = socket.socket(type=socket.SOCK_DGRAM)       # UDP
s.bind(ip_port)                                 # bind
print('....witing for messages...')             #运行时输出
while True:                                     #开始循环
    flag = True
    while flag:
        data, address = s.recvfrom(1024)        #就收数据
        data = data.decode().strip()            #默认接收回来是byte，需要转换成字符串
        s.sendto('hello'.encode(), address)     #发送数据
        print(data)                             #打印接收到的输出
        if data == 'exit':                      #当对端输入exit时，退出
            flag = False
        s.sendto('exit'.encode(), address)      #发送一个exit字符串 给对端
    s.close()                                   #关闭连接


#client
import socket

ip_port = ('127.0.0.1', 8888)

s = socket.socket(type=socket.SOCK_DGRAM)
s.connect(ip_port)
while True:
    messages = input('client: ')
    if messages == 'exit':
        s.close()
        break
    else:
        s.send(messages.encode())
        data = s.recv(1024)
        data = data.decode().strip()
        print(data)
"""