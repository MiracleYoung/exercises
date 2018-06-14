#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/6/13 上午6:14
# @Author  : MiracleYoung
# @File    : al_call_soon.py

import asyncio
import functools

# 下面我们将借助partial函数来说明如何使用关键字参数
def callback(arg, *, kwarg='kwarg'):
    print(f'function callback with {arg} and {kwarg}')

async def main(loop):
    print('register callbacks')
    # 还是通过get_event_loop 获取Eventloop
    loop.call_soon(callback, 'Miracle')
    # 使用partial函数，对kwarg参数进行控制
    wrapped = functools.partial(callback, kwarg='not kwarg')
    loop.call_soon(wrapped, '陈意涵')
    # 上一篇中说过的，await用于等待，sleep也不是time.sleep
    await asyncio.sleep(0.1)

event_loop = asyncio.get_event_loop()
try:
    print('starting event_loop')
    event_loop.run_until_complete(main(event_loop))
finally:
    print('closing event_loop')
    event_loop.close()
