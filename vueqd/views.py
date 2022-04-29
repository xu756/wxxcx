from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json, hashlib, os
from .models import *


# Create your views here.
def login(request):
    res = {}
    if request.method == 'POST':
        getres = json.loads(request.body)
        userinfo = user.objects.filter(username=getres['username'], password=getres['password'])
        if userinfo.exists():
            res['msg'] = '登录成功'
            res['code'] = 200
            token = hashlib.sha1(os.urandom(40)).hexdigest()
            userinfo.update(token=token, is_login=True)
            res['token'] = token
            res['id'] = userinfo[0].id
        else:
            res['code'] = 300
            res['msg'] = '账号或密码错误错误'
        return JsonResponse(res, json_dumps_params={'ensure_ascii': False})
    return JsonResponse({'code': 400, 'msg': '错误，已记录'})