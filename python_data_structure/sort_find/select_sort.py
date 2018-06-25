#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/6/24 上午7:59
# @Author  : MiracleYoung
# @File    : select_sort.py


def select_sort(lst: list):
    _pos_max = 0
    for _n in range(len(lst) -1, 0, -1):
        for _i in range(_n):
            if lst[_i] > lst[_pos_max]:
                _pos_max = _i
        lst[_pos_max], lst[_n] = lst[_n], lst[_pos_max]

    return lst


if __name__ == '__main__':
    lst = [54,26,93,17,77,31,44,55,20]
    print(select_sort(lst))