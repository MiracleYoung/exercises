#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/6/24 下午3:28
# @Author  : MiracleYoung
# @File    : binary_tree.py


class BinaryTree:
    def __init__(self, root):
        self._key = root
        self._left = None
        self._right = None

    def insert_left(self, new_branch):
        if self._left:
            _t = BinaryTree(new_branch)
            _t._left = self._left
            self._left = _t
        else:
            self._left = BinaryTree(new_branch)

    def insert_right(self, new_branch):
        if self._right:
            _t = BinaryTree(new_branch)
            _t._right = self._right
            self._right = _t
        else:
            self._right = BinaryTree(new_branch)

    def get_right_child(self):
        return self._right

    def get_left_child(self):
        return self._left

    def set_root_val(self, val):
        self._key = val

    def get_root_val(self):
        return self._key

    def preorder(self):
        print(self._key)
        if self._left:
            self._left.preorder()
        if self._right:
            self._right.preorder()


if __name__ == '__main__':
    r = BinaryTree('a')
    print(r.get_root_val())
    print(r.get_left_child())
    r.insert_left('b')
    print(r.get_left_child())
    print(r.get_left_child().get_root_val())
    r.insert_right('c')
    print(r.get_right_child())
    print(r.get_right_child().get_root_val())
    r.get_right_child().set_root_val('hello')
    print(r.get_right_child().get_root_val())