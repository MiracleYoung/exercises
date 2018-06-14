#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/13/18 3:07 PM
# @Author  : Miracle Young
# @File    : disorder.py

def disorder_iter(s1, s2):
    _pos1 = 0
    _lst2 = list(s2)
    _ok = True
    while _pos1 < len(s1) and _ok:
        _pos2 = 0
        _found = False
        while _pos2 < len(_lst2) and not _found:
            if s1[_pos1] == _lst2[_pos2]:
                _lst2[_pos2] = None
                _found = True
            else:
                _pos2 += 1

        # if exist one letter does not exist in s2, exit
        if not _found:
            _ok = False

        _pos1 += 1
    return _ok


def disorder_sort(s1, s2):
    _l1, _l2 = list(s1), list(s2)
    _ok = True
    _pos = 0
    _l1.sort()
    _l2.sort()
    while _pos < len(_l1) and _ok:
        if _l1[_pos] == _l2[_pos]:
            _pos += 1
        else:
            _ok = False
    return _ok


def disorder_dict(s1, s2):
    _d1, _d2 = [0] * 26, [0] * 26
    for _, _letter in enumerate(s1):
        _d1[ord(_letter) - ord('a')] += 1

    for _, _letter in enumerate(s2):
        _d2[ord(_letter) - ord('a')] += 1


    _d3, _d4 = {}, {}
    for _, _letter in enumerate(s1):
        _d3[_letter]
    _ok = True

    for i in range(26):
        if _d1[i] == _d2[i]:
            continue
        else:
            _ok = False

    return _ok



if __name__ == '__main__':
    import timeit
    ret = timeit.Timer('disorder_iter("abc", "cba")', "from __main__ import disorder_iter")
    print(ret.timeit(number=10000000))
