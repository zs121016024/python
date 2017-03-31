#!/usr/bin/env python
# coding:utf-8

"""
    通过正则表达式来注册路由

"""

from webob import Request, Response
from webob import exc
from webob.dec import wsgify
import re

class Application:
    ROUTER = []

    @classmethod
    def register(cls, pattern):        #定义一个类装饰器， 传入的参数是 environ内的path路径
        def wrap(handler):          # handler是下面的函数
            cls.ROUTER.append((re.compile(pattern), handler))   #把"通过re.compile匹配到的 pattern(path路径)和handler函数"写入到ROUTER数组内
            return handler          #返回handler函数
        return wrap

    @wsgify
    def __call__(self, request: Request) -> Response:
        for pattern, handler in self.ROUTER:    #对ROUTER数组进行判断是否有pattern和handler
            if pattern.match(request.path):     #如果有match到
                return handler(request)         #返回handler的request内容
        raise exc.HTTPNotFound('not found')     #否则raise一个404

@Application.register('^/hello$')             #装饰器内传入参数 需要用 正则来匹配，以/ 开头， hello结尾
def hello(request: Request) -> Response:
    name = request.params.get("name", 'anonymous')
    response = Response()
    response.text = 'hello {}'.format(name)
    response.status_code = 200
    response.content_type = 'text/plain'
    return response

@Application.register('^/$')                  #装饰器内传入参数 匹配当前路径
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
