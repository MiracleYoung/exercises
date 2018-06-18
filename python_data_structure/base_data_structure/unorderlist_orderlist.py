#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/15/18 3:24 PM
# @Author  : Miracle Young
# @File    : unorderlist.py


class Node:
    def __init__(self, data):
        self._data = data
        self._next = None

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    def set_data(self, data):
        self._data = data

    def set_next(self, data):
        self._next = data


class UnOrderList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def add(self, data):
        _node = Node(data)
        _node.set_next(self._head)
        self._head = _node

    def size(self):
        _current = self._head
        _count = 0
        while _current is not None:
            _current = _current.get_next()
            _count += 1
        return _count

    def search(self, data):
        _current = self._head
        _found = False

        while _current is not None and not _found:
            if _current.get_data() == data:
                _found = True
            else:
                _current = _current.get_next()

        return _found

    def remove(self, data):
        _current, _previous = self._head, None
        _found = False
        # find which one shoule be removed
        while _current is not None and not _found:
            if _current.get_data() == data:
                _found = True
            else:
                _previous = _current
                _current = _current.get_next()
        # remove the target node
        if _previous is None:
            self._head = _current.get_next()
        else:
            _previous.set_next(_current.get_next())


class OrderList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def size(self):
        _current = self._head
        _count = 0

        while _current is not None:
            _current = _current.get_next()
            _count += 1

        return _count

    def remove(self, data):
        _current, _previous = self._head, None
        _found = False

        while _current is not None and not _found:
            if _current.get_data() == data:
                _found = True
            else:
                _previous = _current
                _current = _current.get_next()

        if _previous is None:
            self._head = _current.get_next()
        else:
            _previous.set_next(_current.get_next())

    def search(self, data):
        _current = self._head
        _found, _stop = False, False

        while _current is not None and not _found and not _stop:
            if _current.get_data() == data:
                _found = True
            elif _current.get_data() > data:
                _stop = True
            else:
                _current = _current.get_next()

        return _found

    def add(self, data):
        _current, _previous = self._head, None
        _stop = False

        while _current is not None and not _stop:
            if _current.get_data() > data:
                _stop = True
            else:
                _previous = _current
                _current = _current.get_next()

        _node = Node(data)
        if _previous is None:
            _node.set_next(self._head)
            self._head = _node
        else:
            _node.set_next(_current)
            _previous.set_next(_node)
