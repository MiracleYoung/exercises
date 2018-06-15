#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/15/18 10:25 AM
# @Author  : Miracle Young
# @File    : queue.py


class Queue:
    def __init__(self):
        self._items = []

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def is_empty(self):
        return self._items == []

    def size(self):
        return len(self._items)


