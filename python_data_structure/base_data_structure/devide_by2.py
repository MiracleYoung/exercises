#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/14/18 2:25 PM
# @Author  : Miracle Young
# @File    : devide_by2.py


from python_data_structure.base_data_structure.stack import Stack


def devide_by2(decimal):
    _remstack = Stack()
    while decimal > 0:
        _rem = decimal % 2
        _remstack.push(_rem)
        decimal //= 2

    _ret = ''
    while not _remstack.is_empty():
        _ret += str(_remstack.pop())

    return _ret


def devide_by_base(decimal, base):
    _digits = '0123456789ABCDEF'
    _remstack = Stack()
    while decimal > 0:
        _rem = decimal % base
        _remstack.push(_rem)
        decimal //= base

    _ret = ''
    while not _remstack.is_empty():
        _ret += str(_digits[_remstack.pop()])

    return _ret


if __name__ == '__main__':
    print(devide_by2(233))
    print(devide_by_base(233, 16))
