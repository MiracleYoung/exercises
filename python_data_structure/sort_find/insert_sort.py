#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/6/24 上午8:13
# @Author  : MiracleYoung
# @File    : insert_sort.py


def insert_sort(lst: list):
    for _i in range(1, len(lst)):
        _current_value = lst[_i]
        _idx = _i
        while _idx > 0 and lst[_idx - 1] > _current_value:
            lst[_idx] = lst[_idx - 1]
            _idx -= 1
        lst[_idx] = _current_value
    return lst


if __name__ == '__main__':
    lst = [54,26,93,17,77,31,44,55,20]
    print(insert_sort(lst))