# -*- coding: utf-8 -*-
# @Time    : 2022/4/12 0012 10:13
# @Author  : xu756
# @File    : API.py
import requests
from wxxcx.models import *
from django.core.cache import cache


class wxAPI:
    def __init__(self):
        self.code = None
        self.appid = WxxcConfig.objects.filter(key='AppID').first().value
        self.secret = WxxcConfig.objects.filter(key='AppSecret').first().value

    # 缓存2个小时

    def getAccess_token(self):
        cache.clear()
        access_token = cache.get('access_token')
        if access_token is None:
            params = (
                ('appid', self.appid),
                ('secret', self.secret),
                ('grant_type', 'client_credential'),
            )
            response = requests.post('https://api.weixin.qq.com/cgi-bin/token', params=params)
            access_token = response.json()['access_token']
            res = WxxcConfig.objects.filter(key='access_token').first()
            res.value = access_token
            res.save()
            print('access_token', access_token)
            cache.set('access_token', access_token, 7000)
            return response.json()['access_token']
        else:
            return access_token

    def getsession(self, code):
        self.code = code
        params = (
            ('appid', self.appid),
            ('secret', self.secret),
            ('js_code', self.code),
            ('grant_type', 'authorization_code'),
        )
        response = requests.post('https://api.weixin.qq.com/sns/jscode2session', params=params)
        return response.json()
