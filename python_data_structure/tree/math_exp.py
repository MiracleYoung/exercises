#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/6/24 下午3:58
# @Author  : MiracleYoung
# @File    : math_exp.py

import operator

from python_data_structure.base_data_structure.stack import Stack
from python_data_structure.tree.binary_tree import BinaryTree

def build_parse_tree(exp: str):
    _exp_list = exp.split()
    _stack = Stack()
    _tree = BinaryTree('')
    _stack.push(_tree)
    _current = _tree

    for _item in _exp_list:
        if _item == '(':
            _current.insert_left('')
            _stack.push(_current)
            _current = _current.get_left_child()
        elif _item in ['+', '-', '*', '/']:
            # set current node value
            _current.set_root_val(_item)
            _current.insert_right('')
            _stack.push(_current)
            _current = _current.get_right_child()
        # number
        elif _item not in ['+', '-', '*', '/', ')']:
            _current.set_root_val(int(_item))
            _current = _stack.pop()
        elif _item == ')':
            _current = _stack.pop()
        else:
            raise ValueError
    return _tree


def evaluate(tree: BinaryTree):
    _operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    _left = tree.get_left_child()
    _right = tree.get_right_child()

    if _left and _right:
        _fn = _operators[tree.get_root_val()]
        return _fn(evaluate(_left), evaluate(_right))
    else:
        return tree.get_root_val()


if __name__ == '__main__':
    pt = build_parse_tree("( ( 10 + 5 ) * 3 )")
    print(evaluate(pt))