#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/6/24 下午2:29
# @Author  : MiracleYoung
# @File    : quick_sort.py


def quick_sort(lst: list):
    quick_sort_helper(lst, 0, len(lst) - 1)


def quick_sort_helper(lst: list, first: int, last: int):
    if first < last:
        _pivot = partition(lst, first, last)

        # left sublist
        quick_sort_helper(lst, first, _pivot - 1)
        # right sublist
        quick_sort_helper(lst, _pivot + 1, last)

    print(lst)


def partition(lst: list, first: int, last: int):
    _left_mark, _right_mark = first + 1, last
    _pivot = lst[first]
    _done = False

    while not _done:
        while _left_mark <= _right_mark and lst[_left_mark] <= _pivot:
            _left_mark += 1

        while _right_mark >= _left_mark and lst[_right_mark] >= _pivot:
            _right_mark -= 1

        if _left_mark > _right_mark:
            _done = True
        else:
            lst[_left_mark], lst[_right_mark] = lst[_right_mark], lst[_left_mark]

    lst[first], lst[_right_mark] = lst[_right_mark], lst[first]

    return _right_mark



if __name__ == '__main__':
    lst = [54,26,93,17,77,31,44,55,20]
    quick_sort(lst)
