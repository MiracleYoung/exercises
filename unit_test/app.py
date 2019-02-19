#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/6/18 12:04 PM
# @Author  : Miracle Young
# @File    : app.py


import requests

headers = {
    "content-type": "application/json",
    "Host": "tapdata-server",
    "Origin": "http://tapdata-server",
    "Referer": "http://tapdata-server/login",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36",
}

payload = {
    "username": "arthur@tapdata.io",
    "password": "123456",
    "options": {
        "device": {"platform": "chrome", "platformVersion": "72.0.3626", "sdkVersion": "4.1.1"}
    }
}

res = requests.request(
    method='POST',
    url='http://tapdata-server/api/client/v2.0/app/mongodb-charts-jgejk/auth/providers/local-userpass/login',
    data=payload,
    headers=headers
)
print(res)
