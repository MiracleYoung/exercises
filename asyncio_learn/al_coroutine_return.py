#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/3/1 上午10:29
# @Author  : MiracleYoung
# @File    : app2.py


import asyncio


async def coroutine():
    print('in coroutine')
    # 增加了一个返回值
    return 'result'


event_loop = asyncio.get_event_loop()
try:
    # 有了之前的基础，我们这里就不再单独获取coroutine的对象了
    # run_until_complete会返回coroutine的返回值
    return_value = event_loop.run_until_complete(coroutine())
    print(f'it returned: {return_value}')
finally:
    event_loop.close()
