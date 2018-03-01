#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/3/1 上午10:29
# @Author  : MiracleYoung
# @File    : app2.py


def consumer():
    r = None
    while True:
        n = yield r
        r = 'a' + str(n)

def producer(c):
    n = 0
    next(c)
    while n <= 5:
        n += 1
        r = c.send(n)
        print('producer', str(n))
        print('r', str(r))

c = consumer()
producer(c)
