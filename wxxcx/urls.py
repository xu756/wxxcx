# -*- coding: utf-8 -*-
# @Time    : 2022/4/19 22:26
# @Author  : xu756
# @File    : urls.py
# @Software: IntelliJ IDEA
from django.conf.urls import url
from django.urls import path
from wxxcx import views

urlpatterns = [
    path('getdefault', views.getdefault, name='获取默认页面'),
    path('login', views.login, name='登录'),
    path('feedback', views.feedback, name='意见反馈'),
]
