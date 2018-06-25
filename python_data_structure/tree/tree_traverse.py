#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/6/24 下午5:03
# @Author  : MiracleYoung
# @File    : tree_traverse.py

import operator

from python_data_structure.tree.binary_tree import BinaryTree
from python_data_structure.tree.math_exp import build_parse_tree


def pre_order(tree: BinaryTree):
    if tree:
        print(tree.get_root_val())
        pre_order(tree.get_left_child())
        pre_order(tree.get_right_child())


def post_order(tree: BinaryTree):
    if tree:
        post_order(tree.get_left_child())
        post_order(tree.get_right_child())
        print(tree.get_root_val())


def post_order_eval(tree: BinaryTree):
    _operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    if tree:
        _ret1 = post_order_eval(tree.get_left_child())
        _ret2 = post_order_eval(tree.get_right_child())
        if _ret1 and _ret2:
            return _operators[tree.get_root_val()](_ret1, _ret2)
        else:
            return tree.get_root_val()


def in_order(tree: BinaryTree):
    if tree:
        in_order(tree.get_left_child())
        print(tree.get_root_val())
        in_order(tree.get_right_child())


def print_exp(tree: BinaryTree):
    _s = ''
    if tree:
        _s = '(' + print_exp(tree.get_left_child())
        _s = _s + str(tree.get_root_val())
        _s = _s + print_exp(tree.get_right_child()) + ')'
    return _s

if __name__ == '__main__':
    pt = build_parse_tree("( ( 10 + 5 ) * 3 )")
    print(print_exp(pt))