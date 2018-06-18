#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/15/18 2:09 PM
# @Author  : Miracle Young
# @File    : plaindrome.py


from python_data_structure.base_data_structure.deque import Deque


def plaindrome(s):
    _deque = Deque()
    for _char in s:
        _deque.add_front(_char)

    _ok = True
    while _deque.size() > 1 and _ok:
        _front_char = _deque.remove_front()
        _rear_char = _deque.remove_rear()
        if not _front_char == _rear_char:
            _ok = False

    return _ok


if __name__ == '__main__':
    print(plaindrome('roor'))
    print(plaindrome('rooor'))
    print(plaindrome('roofor'))
