#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/14/18 11:17 AM
# @Author  : Miracle Young
# @File    : app.py


from python_data_structure.base_data_structure.stack import Stack

_stack = Stack()

print(_stack.is_empty())
_stack.push(4)
_stack.push('dog')
print(_stack.peek())
_stack.push(True)
print(_stack.size())
print(_stack.is_empty())
_stack.push(8.4)
print(_stack.pop())
print(_stack.pop())
print(_stack.size())
