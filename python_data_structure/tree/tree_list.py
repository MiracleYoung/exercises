#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/6/24 下午3:18
# @Author  : MiracleYoung
# @File    : tree_list.py


def binary_tree(root):
    return [root, [], []]


def insert_left(root: list, new_branch):
    _t = root.pop(1)
    if len(_t) > 1:
        root.insert(1, [new_branch, _t, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root


def insert_right(root: list, new_branch):
    _t = root.pop(2)
    if len(_t) > 1:
        root.insert(2, [new_branch, [], _t])
    else:
        root.insert(2, [new_branch, [], []])
    return root


def get_root_val(root):
    return root[0]


def set_root_val(root, val):
    root[0] = val


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]
