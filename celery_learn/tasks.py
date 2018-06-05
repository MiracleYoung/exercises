#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/5/18 3:59 PM
# @Author  : Miracle Young
# @File    : tasks.py

from __future__ import absolute_import

from celery_learn.celery import app

@app.task
def add(x, y):
    return x + y

