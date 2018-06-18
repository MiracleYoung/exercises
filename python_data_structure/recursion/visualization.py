#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/6/17 下午3:45
# @Author  : MiracleYoung
# @File    : visualization.py


import turtle

_turtle = turtle.Turtle()
_screen = turtle.Screen()

def draw_spiral(turtle: turtle.Turtle, len):
    if len > 0:
        turtle.forward(len)
        turtle.right(90)
        draw_spiral(turtle, len - 5)


draw_spiral(_turtle, 100)
_screen.exitonclick()
