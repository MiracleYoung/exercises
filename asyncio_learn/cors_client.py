#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/10/30 9:50 PM

__author__ = 'Miracle'


import requests

def req_client(name):
    url = f'http://127.0.0.1:5000/'
    ret = requests.request('GET', url=url)
    return ret

req_client('t1')