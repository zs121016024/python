#!/usr/bin/env python
# coding:utf-8

import webob
from webob.dec import wsgify

@wsgify
def application(request: webob.Request) -> webob.Response:
    if request.path =='/hello':             #如果访问的url后面加上/hello（QUERY_STRING），则打印出hello name
        name = request.params.get("name", "anonymous")
        response = webob.Response()
        response.text = 'hello {}'.format(name)
        response.status_code = 200
        response.content_type = 'text/plain'
        return response
    return webob.Response(body='hello world', content_type='text/plain')    #否则return hello world

if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    server = make_server('0.0.0.0', 8000, application)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()


# /hello?name=zhangsong   => hello zhangsong
# /                       => hello world