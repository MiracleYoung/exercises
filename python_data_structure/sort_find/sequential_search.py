#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/20/18 11:29 AM
# @Author  : Miracle Young
# @File    : sequential_search.py

def seq_search(lst: list, num: int):
    _pos = 0
    _found = False

    while _pos < len(lst) and not _found:
        if lst[_pos] == num:
            _found = True
        else:
            _pos += 1

    return _found


def order_seq_search(lst: list, num: int) -> bool:
    _pos = 0
    _found = False
    _stop = False

    while _pos < len(lst) and not _found and not _stop:
        if lst[_pos] == num:
            _found = True
        elif lst[_pos] > num:
            _stop = True
        else:
            _pos += 1

    return _found


def binary_search(lst: list, num: int) -> bool:
    _first, _last = 0, len(lst) - 1
    _found = False
    while _first <= _last and not _found:
        _mid = (_first + _last) // 2
        if lst[_mid] == num:
            _found = True
        elif lst[_mid] > num:
            _last = _mid - 1
        else:
            _first = _mid + 1

    return _found


def binary_recursive_search(lst: list, num: int) -> bool:
    if len(lst) == 0:
        return False
    else:
        _mid = len(lst) // 2
        if lst[_mid] == num:
            return True
        elif lst[_mid] > num:
            return binary_recursive_search(lst[:_mid], num)
        else:
            return binary_recursive_search(lst[_mid + 1:], num)


if __name__ == '__main__':
    _lst = [1, 2, 3, 5, 6, 12]
    print(seq_search(_lst, 123))
    print(order_seq_search(_lst, 123))
    print(binary_search(_lst, 5))
    print(binary_recursive_search(_lst, 56))
