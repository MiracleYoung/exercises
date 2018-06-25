#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/6/25 上午6:22
# @Author  : MiracleYoung
# @File    : other_module.py

import subprocess

process = subprocess.run(
    ['python', 'app.py', 'miracle'],
    stdin=subprocess.PIPE, stdout=subprocess.PIPE
)
print(process.stdout)
