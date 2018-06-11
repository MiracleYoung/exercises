#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/3/1 上午10:15
# @Author  : MiracleYoung
# @File    : app.py

import asyncio

# asyncio是Python 3.4版本引入的标准库，直接内置了对异步IO的支持。
async def coroutine():
    print('in coroutine')

# asyncio的编程模型就是一个消息循环
# 从asyncio模块中直接获取一个EventLoop的引用
event_loop = asyncio.get_event_loop()
try:
    print('starting coroutine')
    coro = coroutine()
    print('entering event loop')
    # 把需要执行的协程,这里也就是coroutine扔到EventLoop中执行
    event_loop.run_until_complete(coro)
finally:
    print('closing event loop')
    event_loop.close()
