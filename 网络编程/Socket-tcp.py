#!/usr/bin/env python
# coding:utf-8

"""socket 最底层的api

import socket

socket.SOCK_DGRAM   ##udp
socket.SOCK_STREAM  #tcp
socket.SOCK_RAW     #既不是UDP也不是TCP，需要用户空间自己封包，例如 ICMP/网络攻击(SYN)


socket 服务端过程
基本上一个程序对应一个端口，一个线程监听一个socket消息。
正常单线程时，有一个请求连接发来，直接就是由唯一的主线程来监听，
然后发送消息、接收消息，此时若有其它请求来时，则不会处理只能在请求队列等待，
当请求队列已满时则不会再接收请求，直接返回错误。
当第一个请求连接处理完事情后，调用了close方法把客户端连接断开后，才开始读取请求队列里最早的请求，
此时请求队列不是满的，将可以继续接收请求并排队等待被处理

1.初始化socket实例
2.bind  绑定IP和端口
3.listen    设置服务器队列长度
4.accept    监听
5.recv  接收数据
6.send  发送数据

socket 客户端过程
1.初始化socket实例
2.connect

"""

"""
###tcp server/client
import socket
so = socket.socket()  ##创建socket实例
so.bind(('127.0.0.1', 1234))    ###绑定 IP和端口
so.listen(5) ##设置队列长度
s, info = so.accept()  ##监听
while True:
    print(s.recv(1024)) ###accept返回的socket实例，可以接收数据

#s.send(b'1234') ###accept 返回的socket实例， 可以发送数据

#s.close()  ###关闭socket连接
"""



"""
#一个简单的问答小程序
#server:
import socket

sk = socket.socket()                    #创建socket实例
ip_port = ('127.0.0.1', 9002)           #定义IP、端口
sk.bind(ip_port)                        #绑定 IP、端口
sk.listen(5)                             #队列长度

while True:                             # 开始循环接受客户端输出
    conn, address = sk.accept()         # conn 是客户端输入， address是IP和端口
    conn.send('hello'.encode())         # 客户端连接上之后，马上发送一个hello
    flag = True
    while flag:                         # 再次循环
        data = conn.recv(1024).decode() # accept返回的socket实例，接受数据， 并用decode转换
        print(data)                     # 打印出客户端输入
        if data == 'exit':              # 如果客户端输入为exit，则退出
            flag = False
        conn.send('hello'.encode())
    conn.close()                        # 循环执行最后，要close()关闭


#client:
client = socket.socket()                # 初始化实例
ip_port = ('127.0.0.1', 9002)

client.connect(ip_port)

while True:
    data = client.recv(1024).decode()
    print(data)
    inp = input('client: ')
    client.send(inp.encode())
    if inp == 'exit':                   # 判断，如果输入为exit 则退出
        break
"""




