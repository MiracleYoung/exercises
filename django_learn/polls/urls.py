#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 3/2/18 10:36 AM
# @Author  : Miracle Young
# @File    : urls.py

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]