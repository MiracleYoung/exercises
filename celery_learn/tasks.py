#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/5/18 3:59 PM
# @Author  : Miracle Young
# @File    : tasks.py

from __future__ import absolute_import

# from celery import Celery
#
# app = Celery('celery_learn', include=['celery_learn.tasks'])
#
# app.config_from_object('celery_learn.celeryconfig')
#
# if __name__ == '__main__':
#     app.start()


from celery import Celery

app = Celery('tasks', backend='redis://localhost', broker='redis://localhost')
app.config_from_object('celeryconfig')

@app.task
def add(x, y):
    return x + y