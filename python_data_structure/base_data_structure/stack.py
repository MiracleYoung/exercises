#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/14/18 11:14 AM
# @Author  : Miracle Young
# @File    : stack.py

class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return self._items == []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[len(self._items) - 1]

    def size(self):
        return len(self._items)