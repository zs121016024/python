#!/usr/bin/env python
# coding:utf-8

"""
wsgify装饰器的作用：把一个普通的函数，转变成WSGI应用程序
"""

import webob
from webob.dec import wsgify


@wsgify         #wsgify装饰器
def application(request: webob.Request) -> webob.Response:     #程序
    name = request.params.get("name", "anonymous")              #通过wsgify装饰器，获取到request请求，并获取url后面的参数

    response = webob.Response()
    response.text = 'hello {}'.format(name)                     #输出
    response.status_code = 200                                  #状态码
    response.content_type = 'text/plain'                        #类型
    return response                                             #返回

if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    server = make_server('0.0.0.0', 8000, application)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()

