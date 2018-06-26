#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/25/18 10:54 AM
# @Author  : Miracle Young
# @File    : binary_heap.py

class BinaryHeap:
    def __init__(self):
        self._heap_list = []
        self._size = 0

    def perc_up(self, size):
        while size // 2 > 0:
            if self._heap_list[size] < self._heap_list[size // 2]:
                self._heap_list[size], self._heap_list[size // 2] = self._heap_list[size // 2], self._heap_list[size]
            size // 2

    def insert(self, i):
        self._heap_list.append(i)
        self._size += 1
        self.perc_up(self._size)

    def find_min(self, i):
        pass

    def perc_down(self, pos):
        while pos * 2 <= self._size:
            _mc = self.min_child(pos)
            if self._heap_list[pos] > self._heap_list[_mc]:
                self._heap_list[pos], self._heap_list[_mc] = self._heap_list[_mc], self._heap_list[pos]
            pos = _mc



    # find pos's max(maxchild, minchild)
    def min_child(self, pos):
        if pos * 2 + 1 > self._size:
            return pos * 2
        else:
            if self._heap_list[pos * 2] < self._heap_list[pos * 2 + 1]:
                return pos * 2
            else:
                return pos * 2 + 1

    def del_min(self):
        _del_val = self._heap_list[1]
        self._heap_list[1] = self._heap_list[self._size]
        self._size -= 1
        self._heap_list.pop()
        self.perc_down(1)
        return _del_val

    def is_empty(self):
        pass

    def size(self):
        pass

    def build_heap(self, lst):
        print(f'Start ordering... {lst}')
        _pos = len(lst) // 2
        self._size = len(lst)
        self._heap_list = [0] + lst
        while _pos > 0:
            self.perc_down(_pos)
            _pos -= 1
        print(f'List ordered: {self._heap_list}')


if __name__ == '__main__':
    bh = BinaryHeap()
    bh.build_heap([9, 5, 6, 2, 3])
    print(bh.del_min())
    print(bh.del_min())
    print(bh.del_min())
    print(bh.del_min())
    print(bh.del_min())