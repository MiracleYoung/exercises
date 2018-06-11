#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/5/18 3:52 PM
# @Author  : Miracle Young
# @File    : app.py

# from celery import Celery, platforms
#
# platforms.C_FORCE_ROOT = True  #加上这一行
#

from celery_learn.tasks import add

add.delay(4, 4)