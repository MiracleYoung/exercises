#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/15/18 10:37 AM
# @Author  : Miracle Young
# @File    : joseph_question.py


from python_data_structure.base_data_structure.queue import Queue


def joseph_question(roll_list, num):
    _q = Queue()
    for _item in roll_list:
        _q.enqueue(_item)

    while _q.size() > 1:
        for _ in range(num):
            _q.enqueue(_q.dequeue())

        _q.dequeue()

    return _q.dequeue()


if __name__ == '__main__':
    print(joseph_question(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))