#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/6/17 下午4:00
# @Author  : MiracleYoung
# @File    : tree.py

import turtle

def tree(turtle: turtle.Turtle, len):
    if len > 5:
        turtle.forward(len)
        turtle.right(20)
        tree(turtle, len - 15)
        turtle.left(40)
        tree(turtle, len - 10)
        turtle.right(20)
        turtle.backward(len)


def main():
    _turtle = turtle.Turtle()
    _screen = turtle.Screen()
    _turtle.left(90)
    _turtle.up()
    _turtle.backward(100)
    _turtle.down()
    _turtle.color('green')
    tree(_turtle, 75)
    _screen.exitonclick()

main()