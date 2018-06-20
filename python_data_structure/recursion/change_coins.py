#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/19/18 2:45 PM
# @Author  : Miracle Young
# @File    : change_coins.py


def change_coins(coins: list, change: int):
    _min_coins = change
    if change in coins:
        return 1
    else:
        for _item in [c for c in coins if c <= change]:
            _counts = 1 + change_coins(coins, change - _item)
            if _counts < _min_coins:
                _min_coins = _counts
    return _min_coins


def change_coins_v2(coins: list, change: int, result: list):
    _min_coins = change
    if change in coins:
        result[change] = 1
        return 1
    elif result[change] > 0:
        return result[change]
    else:
        for _item in [c for c in coins if c <= change]:
            _counts = 1 + change_coins_v2(coins, change - _item, result)
            if _counts < _min_coins:
                _min_coins = _counts
                result[change] = _min_coins
    return _min_coins


def dp_change_coins(coins: list, change: int, min_coins: list):
    for _cents in range(change + 1):
        _counts = _cents
        for j in [c for c in coins if c <= _cents]:
            if min_coins[_cents - j] + 1 < _counts:
                _counts = min_coins[_cents - j] + 1
        min_coins[_cents] = _counts
    return min_coins[change]


if __name__ == '__main__':
    print(dp_change_coins([1, 5, 10, 25], 63, [0] * 64))
