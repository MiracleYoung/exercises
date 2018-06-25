#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/6/24 上午7:37
# @Author  : MiracleYoung
# @File    : bubble_sort.py


def bubble_sort(lst: list):
    for _n in range(len(lst) - 1, 0, -1):
        for _i in range(_n):
            if lst[_i] > lst[_i + 1]:
                lst[_i], lst[_i + 1] = lst[_i + 1], lst[_i]
    return lst


def short_bubble_sort(lst: list):
    _n = len(lst) - 1
    _exchange = True
    while _n > 0 and _exchange:
        _exchange = False
        for _i in range(_n):
            if lst[_i] > lst[_i + 1]:
                _exchange = True
                lst[_i], lst[_i + 1] = lst[_i + 1], lst[_i]

        _n -= 1
    return lst


if __name__ == '__main__':
    lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    lst2= [20,30,40,90,50,60,70,80,100,110]
    print(bubble_sort(lst))
    print(short_bubble_sort(lst2))
