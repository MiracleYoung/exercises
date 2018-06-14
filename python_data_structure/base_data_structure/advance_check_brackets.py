#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/14/18 1:44 PM
# @Author  : Miracle Young
# @File    : advance_check_brackets.py

from python_data_structure.base_data_structure.stack import Stack


def check_brackets(s):
    _stack = Stack()
    _ok = True
    _index = 0
    while _index < len(s) and _ok:
        if s[_index] in '([{':
            _stack.push(s[_index])
        else:
            if _stack.is_empty():
                _ok = False
                return _ok
            else:
                _open = _stack.pop()
                # s[_index] is close symbol
                if not matches(_open, s[_index]):
                    _ok = False
                    return _ok
        _index += 1
    return _ok and _stack.is_empty()


def matches(open, close):
    _opens, _closes = '([{', ')]}'
    return _opens.index(open) == _closes.index(close)


if __name__ == '__main__':
    print(check_brackets('({[(){[]}]})'))
    print(check_brackets('({[(){]}]})'))
