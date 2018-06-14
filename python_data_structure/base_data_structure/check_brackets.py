#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/14/18 11:38 AM
# @Author  : Miracle Young
# @File    : check_brackets.py


from python_data_structure.base_data_structure.stack import Stack

def check_par_brackets(s):
    _stack = Stack()
    _ok = True
    _index = 0
    while _index < len(s) and _ok:
        _item = s[_index]
        if _item == '(':
            _stack.push(_item)
        else:
            if _stack.is_empty():
                _ok = False
                return _ok
            else:
                _stack.pop()
        _index += 1
    # _stack must be empty
    return _ok and _stack.is_empty()


if __name__ == '__main__':
    print(check_par_brackets('((())(())'))
