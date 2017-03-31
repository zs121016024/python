#!/usr/bin/env python
# coding:utf-8

from urllib.parse import parse_qs   #导入urllib库

def application(environ: dict, start_response):     #程序
    params = parse_qs(environ['QUERY_STRING'])  # 获取QUERY_STRING参数
    name = params.get('name', ['anonymous'])[0]     #获取参数后的name ，默认为anonymous
    start_response('200 ok', [('Content-Type', 'text/plain')])  #显示headers
    return ["hello {}".format(name).encode()]  #显示body体

if __name__ == '__main__':
    from wsgiref.simple_server import make_server       #调用make_server模块

    server = make_server('0.0.0.0', 8000, application)  #绑定 iP、端口、程序

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()

"""
访问时URL:
    http://127.0.0.1:8000/?name=zhangsong
"""