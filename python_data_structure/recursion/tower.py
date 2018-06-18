#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/6/17 下午5:48
# @Author  : MiracleYoung
# @File    : tower.py


def move_tower(height,fromPole, toPole, withPole):
    if height >= 1:
        move_tower(height-1,fromPole,withPole,toPole)
        move_disk(fromPole,toPole)
        move_tower(height-1,withPole,toPole,fromPole)

def move_disk(fp,tp):
    print("moving disk from",fp,"to",tp)


move_tower(6, 'A', 'C', 'B')