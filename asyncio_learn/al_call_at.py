#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/6/13 上午6:30
# @Author  : MiracleYoung
# @File    : al_call_at.py

import asyncio
import time


def callback(n, loop):
    print(f'callback with {n} at {loop.time()}')

async def main(loop):
    # 使用loop.time 而不是time和datetime模块
    now = loop.time()
    print(f'time模块的时间: {time.time()}')
    print(f'loop.time的时间: {now}')

    print('register callbacks')
    # 使用call_at指定当前时间后的0.2秒执行
    # 执行完了回掉callback
    # callback的n和loop参数
    loop.call_at(now + 0.2, callback, 1, loop)
    loop.call_at(now + 0.1, callback, 2, loop)
    # 和call_soon对比一下
    loop.call_soon(callback, 3, loop)

    await asyncio.sleep(1)


event_loop = asyncio.get_event_loop()
try:
    print('starting event_loop')
    event_loop.run_until_complete(main(event_loop))
finally:
    print('closing event_loop')
    event_loop.close()
