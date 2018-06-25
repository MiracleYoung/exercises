#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/6/24 上午9:51
# @Author  : MiracleYoung
# @File    : merge_sort.py


def merge_sort(lst: list):
    print(f'Splitting {lst}')
    if len(lst) > 1:
        _i, _j, _k = 0, 0, 0
        _mid = len(lst) // 2
        _lh, _rh = lst[:_mid], lst[_mid:]

        merge_sort(_lh)
        merge_sort(_rh)

        while _i < len(_lh) and _j < len(_rh):
            if _lh[_i] < _rh[_j]:
                lst[_k] = _lh[_i]
                _i += 1
            else:
                lst[_k] = _rh[_j]
                _j += 1
            _k += 1

        while _j < len(_rh):
            lst[_k] = _rh[_j]
            _j += 1
            _k += 1

        while _i < len(_lh):
            lst[_k] = _lh[_i]
            _i += 1
            _k += 1

    print(f'Merging {lst}')


if __name__ == '__main__':
    lst = [54,26,93,17,77,31,44,55,20]
    print(merge_sort(lst))