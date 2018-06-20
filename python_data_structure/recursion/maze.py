#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/19/18 11:10 AM
# @Author  : Miracle Young
# @File    : maze.py


import turtle

PART_OF_PATH = 'O'
TRIED = '.'
OBSTACLE = '+'
DEAD_END = '-'


def search_from(maze, start_row, start_column):
    maze.updatePosition(start_row, start_column)
    if maze[start_row][start_column] == OBSTACLE:
        return False

    if maze[start_row][start_column] == TRIED:
        return False

    if maze.isExit(start_row, start_column):
        maze.updatePosition(start_row, start_column, PART_OF_PATH)
        return True
    maze.updatePosition(start_row, start_column, TRIED)

    # Otherwise, use logical short circuiting to try each
    # direction in turn (if needed)
    found = search_from(maze, start_row - 1, start_column) or \
            search_from(maze, start_row + 1, start_column) or \
            search_from(maze, start_row, start_column - 1) or \
            search_from(maze, start_row, start_column + 1)
    if found:
        maze.updatePosition(start_row, start_column, PART_OF_PATH)
    else:
        maze.updatePosition(start_row, start_column, DEAD_END)
    return found


class Maze:
    def __init__(self, maze_file):
        self._mazelist = []
        for _r, _line in enumerate(open(maze_file, 'r')):
            _rowlist = []
            for _j, _ch in enumerate(_line[:-1]):
                _rowlist.append(_ch)
                if _ch == 'S':
                    self._start_row = _r
                    self._start_col = _j

            self._mazelist.append(_rowlist)
        _rows_in_maze = _r
        _cols_in_maze = len(_rowlist)

        self._rows_in_maze = _rows_in_maze
        self._cols_in_maze = _cols_in_maze
        self._x = _cols_in_maze / 2
        self._y = _rows_in_maze / 2
        self._turtle = turtle.Turtle(shape='turtle')
        self._wn = turtle.Screen()

        self._wn.set_world_coordinates(-(_cols_in_maze - 1) / 2 - .5,
                              -(_rows_in_maze - 1) / 2 - .5,
                              (_cols_in_maze - 1) / 2 + .5,
                              (_rows_in_maze - 1) / 2 + .5)

    def draw_maze(self):
        for _r in range(self._rows_in_maze):
            for _j in range(self._cols_in_maze):
                if self._mazelist[_r][_j] == OBSTACLE:
                    self.draw_center_box(_j + self._x, -_r + self._y, 'tan')
        self._turtle.color('black', 'blue')

    def draw_center_box(self, x, y, color):
        self._turtle.up()
        self._turtle.goto(x - .5, y - .5)
        self._turtle.color('black', color)
        self._turtle.setheading(90)
        self._turtle.down()
        self._turtle.begin_fill()
        for _i in range(4):
            self._turtle.forward(1)
            self._turtle.right(90)
        self._turtle.end_fill()

    def move_turtle(self, x, y):
        self._turtle.up()
        self._turtle.setheading(self._turtle.towards(x + self._x, y + self._y))
        self._turtle.goto(x + self._x, -y + self._y)

    def drop_breadcrumb(self, color):
        self._turtle.dot(color)

    def update_position(self, row, col, val=None):
        if val:
            self._mazelist[row][col] = val
        self.move_turtle(col, row)

        if val == PART_OF_PATH:
            _color = 'green'
        elif val == OBSTACLE:
            _color = 'red'
        elif val == TRIED:
            _color = 'black'
        elif val == DEAD_END:
            _color = 'red'
        else:
            _color = None

        if _color:
            self.drop_breadcrumb(_color)

    def is_exit(self, row, col):
        return (row == 0
                or row == self._rows_in_maze - 1
                or col == 0
                or col == self._cols_in_maze - 1)

    def __getitem__(self, item):
        return self._mazelist[item]

myMaze = Maze('maze_sample.txt')
myMaze.draw_maze()
myMaze.update_position(myMaze._start_row,myMaze._start_col)

search_from(myMaze, myMaze._start_row, myMaze._start_col)