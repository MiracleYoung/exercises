#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/6/17 下午3:11
# @Author  : MiracleYoung
# @File    : int2str.py

def int2str(num: int, base: int):
    _ref = '0123456789ABCDEF'
    if num < base:
        return _ref[num]
    else:
        return int2str(num // base, base) + _ref[num % base]


from python_data_structure.base_data_structure.stack import Stack


def int2str_by_stack(num: int, base: int):
    _stack = Stack()
    _ref = '0123456789ABCDEF'
    while num > 0:
        if num < base:
            _stack.push(_ref[num])
        else:
            _stack.push(_ref[num % base])
        num //= base

    _ret = ''
    while not _stack.is_empty():
        _ret += str(_stack.pop())

    return _ret


if __name__ == '__main__':
    print(int2str(2748, 16))
    print(int2str_by_stack(2748, 16))
