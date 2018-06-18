#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/6/17 下午4:42
# @Author  : MiracleYoung
# @File    : Sierpinski.py


import turtle


def draw_triangle(points, color, turtle: turtle.Turtle):
    turtle.fillcolor(color)
    turtle.up()
    turtle.goto(points[0][0], points[0][1])
    turtle.down()
    turtle.begin_fill()
    turtle.goto(points[1][0], points[1][1])
    turtle.goto(points[2][0], points[2][1])
    turtle.goto(points[0][0], points[0][1])
    turtle.end_fill()


def get_mid(p1, p2):
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2


def sierpinski(points, degree, turtle: turtle.Turtle):
    _color_map = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    draw_triangle(points, _color_map[degree], turtle)
    if degree > 0:
        sierpinski([points[0], get_mid(points[0], points[1]), get_mid(points[0], points[2])], degree - 1, turtle)
        sierpinski([points[1], get_mid(points[1], points[0]), get_mid(points[1], points[2])], degree - 1, turtle)
        sierpinski([points[2], get_mid(points[2], points[1]), get_mid(points[2], points[0])], degree - 1, turtle)

def main():
    _turtle = turtle.Turtle()
    _screen = turtle.Screen()
    _points = [[-100, -50], [0, 100], [100, -50]]
    sierpinski(_points, 3, _turtle)
    _screen.exitonclick()

main()