#!/usr/bin/env python
# coding:utf-8

"""
    通过装饰器来注册路由

"""

from webob import Request, Response
from webob import exc
from webob.dec import wsgify

class Application:
    ROUTER = {}

    @classmethod
    def register(cls, path):        #定义一个类装饰器， 传入的参数是 environ内的path路径
        def wrap(handler):          # handler是下面的函数
            cls.ROUTER[path] = handler      # path为key, handler为value 写入字典
            #print('{} = > {}'.format(path, handler))    通过打印出来，可查看到，path为ROUTER字典内的key, handler为ROUTER字典内的value
            return handler
        return wrap

    @wsgify
    def __call__(self, request: Request) -> Response:
        try:
            return self.ROUTER[request.path](request)
        except KeyError:
            raise exc.HTTPNotFound('not found')

@Application.register('/hello')             #装饰器内传入参数 path
def hello(request: Request) -> Response:
    name = request.params.get("name", 'anonymous')
    response = Response()
    response.text = 'hello {}'.format(name)
    response.status_code = 200
    response.content_type = 'text/plain'
    return response

@Application.register('/')                  #装饰器内传入参数 /
def index(request: Request) -> Response:
    return Response(body='hello world', content_type='text/plain')

if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    server = make_server('0.0.0.0', 8888, Application())
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()


# /hello?name=zhangsong   => hello zhangsong
# /                       => hello world