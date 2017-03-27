#!/usr/bin/env python
# coding:utf-8

import os
from urllib.parse import parse_qs

def appliction(environ:dict, start_response):   #start_response为输出  # environ为用户的输入
    params = parse_qs(environ['QUERY_STRING'])
    name = params.get('name',['anonymous'])[0]
    print(name)
    #biz
    start_response('200 OK', [('Content-Type', 'text/plain')]) #headers
    return ["hello world".encode()] #body


if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    server = make_server('0.0.0.0', 8000, appliction)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()