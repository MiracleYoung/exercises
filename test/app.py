#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/6/18 12:04 PM
# @Author  : Miracle Young
# @File    : app.py


class Int:
    def __init__(self, name):
        self.name = name
        self.data = {}

    def __get__(self, instance, cls):
        print('get {}'.format(self.name))
        if instance is not None:
            return self.data[instance]
        return self

    def __set__(self, instance, value):
        self.data[instance] = value


class A:
    # 这里定义一个类变量
    val = Int('val')

    def __init__(self):
        # 在定义一个A的实例变量
        self.val = 3


a = A()
a.val
