#!/usr/bin/env python
# coding:utf-8

from webob import Request, Response   # pip安装webob模块
from webob.dec import wsgify          #下面需要用到wsgify装饰器

def hello(request: Request) -> Response:    #定义函数hello,
    name = request.params.get("name", 'anonymous')
    response = Response()
    response.text = 'hello {}'.format(name)
    response.status_code = 200
    response.content_type = 'text/plain'
    return response                 #返回response

def index(request: Request) -> Response:    #定义函数 index
    return Response(body='hello wrold', content_type='text/plain')

class Application:
    ROUTER = {}

    @classmethod                                                #用classmethod装饰器，方便下面直接通过 类.方法 调用
    def register(cls, path, handler):
        cls.ROUTER[path] = handler

    def default_hander(self, request: Request) -> Response:
        return Response(body='not found', status=404)

    @wsgify
    def __call__(self, request: Request) -> Response:               #用__call__方法，方便之后调用
        return self.ROUTER.get(request.path, self.default_hander)(request)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    server = make_server('0.0.0.0', 8888, Application())      #定义bind的IP、端口、调用__call__方法函数

    Application.register('/hello', hello)           #路由注册
    Application.register('/', index)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()




