#!/usr/bin/env python
# coding:utf-8

from webob import Request, Response   # pip安装webob模块
from webob.dec import wsgify          #下面需要用到wsgify装饰器
from webob import exc                 #导入exc模块，目的是用于以下直接返回HTTP状态码


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
        cls.ROUTER[path] = handler                              #path作为key  handler作为value

    @wsgify
    def __call__(self, request: Request) -> Response:               #用__call__方法，方便之后调用
        try:
            return self.ROUTER[request.path](request)
        except KeyError:
            raise exc.HTTPNotFound('not found')                     #返回错误信息

if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    server = make_server('0.0.0.0', 8888, Application())      #定义bind的IP、端口、调用__call__方法函数

    Application.register('/hello', hello)           #路由注册
    Application.register('/', index)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()


# /hello?name=zhangsong   => hello zhangsong
# /                       => hello world




