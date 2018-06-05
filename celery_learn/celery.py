#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/5/18 3:59 PM
# @Author  : Miracle Young
# @File    : celery.py

from __future__ import absolute_import, unicode_literals

from celery import Celery

app = Celery('celery_learn', include=['celery_learn.tasks'])

app.config_from_object('celery_learn.celeryconfig')

if __name__ == '__main__':
    app.start()