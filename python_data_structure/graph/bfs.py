#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/27/18 2:39 PM
# @Author  : Miracle Young
# @File    : bfs.py


from python_data_structure.graph.graphs import Graph, Vertex
from python_data_structure.base_data_structure.queue import Queue


def bfs(g: Graph, start: Vertex):
    start.set_distance(0)
    start.set_pred(None)
    _vert_queue = Queue()
    _vert_queue.enqueue(start)
    while _vert_queue.size() > 0:
        _current_vert = _vert_queue.dequeue()
        for _nbr in _current_vert.get_connections():
            if _nbr.get_color() == 'white':
                _nbr.set_color('gray')
                _nbr.set_distance(_current_vert.get_distance() + 1)
                _nbr.set_pred(_current_vert)
                _vert_queue.enqueue(_nbr)
            _current_vert.set_color('black')
