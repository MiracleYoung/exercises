#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/6/24 上午9:18
# @Author  : MiracleYoung
# @File    : shell_sort.py


def shell_sort(lst: list):
    _sublist_count = len(lst) // 2
    while _sublist_count > 0:
        for _start in range(_sublist_count):
            gap_insert(lst, _start, _sublist_count)

        print(f'After increments of size {_sublist_count}, The list is {lst}')

        _sublist_count //= 2


def gap_insert(lst: list, start: int, gap: int):
    for _i in range(start + gap, len(lst), gap):
        _current_value = lst[_i]
        _pos = _i

        while _pos >= gap and lst[_pos - gap] > _current_value:
            lst[_pos] = lst[_pos - gap]
            _pos -= gap

        lst[_pos] = _current_value


if __name__ == '__main__':
    lst = [54,26,93,17,77,31,44,55,20]
    print(shell_sort(lst))