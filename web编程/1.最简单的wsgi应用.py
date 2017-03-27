#!/usr/bin/env python
# coding:utf-8

def application(environ, start_response):   #定义程序， environ 为用户输入， start_response为用户输出
    # 下面为程序
    start_response('200 OK', [('Content-Type', 'text/plain')]) # 显示的Header头
    return ["hello world".encode()] # 显示的body体


if __name__ == '__main__':
    from wsgiref.simple_server import make_server       #测试时候，一般用make_server模块
    server = make_server('0.0.0.0', 8000, application)  #定义ip、端口、程序
    try:
        server.serve_forever()  #启动服务
    except KeyboardInterrupt:
        server.shutdown()       #关闭服务