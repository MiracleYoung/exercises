#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/27/18 2:02 PM
# @Author  : Miracle Young
# @File    : word_ladder.py

from python_data_structure.graph.graphs import Graph


def build_graph(word_file):
    _d = {}
    _g = Graph()
    _wfile = open(word_file, 'r')
    for _line in _wfile:
        _word = _line[:-1]
        for i in range(len(_word)):
            _bucket = _word[:i] + '_' + _word[i + 1:]
            if _bucket in _d:
                _d[_bucket].append(_word)
            else:
                _d[_bucket] = _word
    for _bucket in _d.keys():
        for w1 in _d[_bucket]:
            for w2 in _d[_bucket]:
                if w1 != w2:
                    _g.add_edge(w1, w2)

    return _g
