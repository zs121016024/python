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

router = {          #定义静态路由
    '/hello': hello,       #如果访问的是 /hello, 则路由到 hello函数，并返回
    '/': index              # 如果访问的是/（正常访问，不加任何参数）， 则路由到index函数，并返回
}

@wsgify
def application(request: Request) -> Response:
    return router.get(request.path, index)(request)     #返回静态路由访问到的函数

if __name__ == '__main__':
    from  wsgiref.simple_server import make_server

    server = make_server('0.0.0.0', 8888, application)      #定义bind的IP、端口、
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()




