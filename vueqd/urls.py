# -*- coding: utf-8 -*-
# @Time    : 2022/4/17 0017 11:06
# @Author  : xu756
# @File    : urls.py
from django.conf.urls import url
from django.urls import path
from vueqd import views

urlpatterns = [
    path('login', views.login),
]
