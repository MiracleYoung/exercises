#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/6/25 上午6:18
# @Author  : MiracleYoung
# @File    : exec_othermodule_main.py

import sys


def main(args):
    print(args)


if __name__ == '__main__':
    print("执行如下代码 __name__ == '__main__'")
    # 参数随便指定即可
    main(sys.argv[1:])
