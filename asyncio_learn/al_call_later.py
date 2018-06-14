#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/6/13 上午6:25
# @Author  : MiracleYoung
# @File    : al_call_later.py

import asyncio

def callback(n):
    print(f'callback with {n}')


async def main(loop):
    print('register callbacks')
    # 延迟0.2秒执行
    # 执行完后调用callback函数
    # callback的参数n
    loop.call_later(0.2, callback, 1)
    loop.call_later(0.1, callback, 2)
    # 再来看下和call_soon的区别
    loop.call_soon(callback, 3)

    await asyncio.sleep(0.4)

event_loop = asyncio.get_event_loop()
try:
    print('starting event_loop')
    event_loop.run_until_complete(main(event_loop))
finally:
    print('closing event_loop')
    event_loop.close()