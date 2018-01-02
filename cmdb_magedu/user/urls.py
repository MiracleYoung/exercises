#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/1/2 上午6:50
# @Author  : MiracleYoung
# @File    : urls.py

from django.conf.urls import url
from . import views

app_name = 'user'

urlpatterns = [
    url(r'^$', views.index, name='user'),
    url(r'^login/$', views.login, name='login'),
    url(r'^users/$', views.users, name='users'),

]