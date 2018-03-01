#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/3/1 上午10:15
# @Author  : MiracleYoung
# @File    : app.py

def consumer():
    r = None
    while True:
        # 2.consumer通过yield拿到传递的None，yield跳出
        n = yield r
        # 4.从上次跳出的位置，接着往下执行
        if not n:
            return
        print('[CONSUMER] Consuming %s ...' % n )
        r = '200 OK' + str(n)
        # 6.从这里开始循环，到yield的时候，再跳出来

def produce(c):
    # 1.启动生成器，会跳到consumer
    next(c)
    # 3.接着往下执行，产生数据，通过c.send(n)，再切换到consumer
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s ...' % n )
        r = c.send(n)
        # 7.跳出来后，函数返回值是200 OK，所以往下执行，print出200 OK
        print('[PRODUCER Consumer return: %s' % r)
        # 8.从这里开始循环前面的步骤，直到最后
    c.close()

c = consumer()
produce(c)