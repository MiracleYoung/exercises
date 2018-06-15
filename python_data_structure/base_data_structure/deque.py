#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/15/18 1:42 PM
# @Author  : Miracle Young
# @File    : deque.py

class Deque:
    def __init__(self):
        self._items = []

    def add_front(self, item):
        self._items.append(item)

    def add_rear(self, item):
        self._items.insert(0, item)

    def remove_front(self):
        return self._items.pop()

    def remove_rear(self):
        return self._items.pop(0)

    def is_empty(self):
        return self._items == []

    def size(self):
        return len(self._items)

