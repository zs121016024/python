#!/usr/bin/env python
# coding:utf-8

import os
def application(environ: dict, start_response):   # environ是一个字典类型
    for k, v in environ.items():
        if k not in os.environ.keys():          #过滤系统自带的os.environ.key
            print("{} => {}".format(k, v))        #通过打印看出，environ返回的是用户相关的消息
    start_response('200 OK', [('Content-Type', 'text/plain')]) # 显示的headers
    return ["hello world".encode()] # 显示的body体


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('0.0.0.0', 8000, application)      #绑定 ip/端口/程序
    try:
        server.serve_forever()  #启动服务
    except KeyboardInterrupt:
        server.shutdown()       #关闭服务

"""
访问时URL：
    127.0.0.1:8000
"""