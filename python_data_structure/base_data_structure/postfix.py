#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/14/18 3:34 PM
# @Author  : Miracle Young
# @File    : postfix.py


import string

from python_data_structure.base_data_structure.stack import Stack


def infix2prefix(s: str):
    _priority = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }
    _ret = []
    _opstack = Stack()
    _srclst = s.split()
    _refer = string.ascii_uppercase + string.digits
    _index = 0
    while _index < len(_srclst):
        _item = _srclst[_index]
        if _item == '(':
            _opstack.push(_item)
        elif _item in _refer:
            _ret.append(_item)
        elif _item == ')':
            _top = _opstack.pop()
            # maybe exist multi operations rather than one.
            # so need to add continually until meet '('
            while _top != '(':
                _ret.append(_top)
                _top = _opstack.pop()
        else:
            while (not _opstack.is_empty()) and _priority[_opstack.peek()] >= _priority[_item]:
                _ret.append(_opstack.pop())
            _opstack.push(_item)
        _index += 1

    while not _opstack.is_empty():
        _ret.append(_opstack.pop())

    return ''.join(_ret)


def postfix_math(s: str):
    _stack = Stack()
    _srclst = s.split()
    _refer = string.digits
    for _item in _srclst:
        if _item in _refer:
            _stack.push(int(_item))
        else:
            _op1 = int(_stack.pop())
            _op2 = int(_stack.pop())
            # op2 operator op1
            _value = calc(_item, _op2, _op1)
            _stack.push(_value)

    return _stack.pop()


def calc(op, n1, n2):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    else:
        return n1 / n2


if __name__ == '__main__':
    print(infix2prefix('( A + B ) * ( C + D )'))
    print(infix2prefix('( A + B ) * C'))
    print(infix2prefix('A + B * C'))
    print(postfix_math('7 8 + 3 2 + /'))
