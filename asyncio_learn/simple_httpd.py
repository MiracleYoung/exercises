#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/10/30 10:11 PM

__author__ = 'Miracle'

from wsgiref.simple_server import make_server

import time, logging, threading

logging.basicConfig(format='%(threadName)s %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__file__)

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:

def fn():
    logger.info('threading start')
    time.sleep(10)
    logger.info('threading end.')

def application(environ, start_response):
    logger.info('receive response')
    t = threading.Thread(target=fn, args=(), daemon=True)
    t.start()
    t.join()
    start_response('200 OK', [('Content-Type', 'text/html')])
    logger.info('end response')
    return [b'<h1>Hello, web!</h1>']


httpd = make_server('', 5000, application)
print("Serving HTTP on port 5000...")
httpd.serve_forever()
