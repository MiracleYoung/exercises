#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/6/12 上午6:41
# @Author  : MiracleYoung
# @File    : al_coroutine_multi.py

import asyncio

# 函数1
async def one():
    print('in one')
    asyncio.sleep(1)
    print('one end')
    return 'one'

# 函数2
async def two(arg):
    print('in two')
    asyncio.sleep(1)
    print('two end')
    return 'two with arg {}'.format(arg)

# 将作为coroutine
async def outer():
    print('in outer')
    print('waiting for one')
    # 等待函数1的返回值
    result1 = await one()
    print('waiting for two')
    # 等待函数2的返回值
    result2 = await two(result1)
    # 将2个结果一并返回
    return result1, result2


event_loop = asyncio.get_event_loop()
try:
    return_value = event_loop.run_until_complete(outer())
    print(f'result value: {return_value}')
finally:
    event_loop.close()
