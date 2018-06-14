#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/13/18 4:22 PM
# @Author  : Miracle Young
# @File    : dct.py

import timeit
import random

for i in range(10000, 10000001, 20000):
    ret = timeit.Timer("random.randrange(%d) in x" % i, "from __main__ import random, x")
    x = list(range(i))
    lst_time = ret.timeit(number=1000)
    x = {j: None for j in range(i)}
    d_time = ret.timeit(number=1000)
    print("%d, %10.3f, %10.3f" % (i, lst_time, d_time))