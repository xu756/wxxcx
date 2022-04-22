from django.http import JsonResponse
from django.shortcuts import render
from django_api_cache import api_cache
from django.views.decorators.cache import cache_page
from .models import *

from wxxcx.methods.API import wxAPI


# Create your views here.
def index(request):
    a = {'name': '传入数据'}
    # l = message(user_id=1, content='你好')
    # l.save()
    return render(request, 'index.html', a)


# 获取轮播图
@cache_page(60)
def getswiper(request):
    res, meta = {}, {}
    res['data'] = list(swiper.objects.all().values())[:3]
    return JsonResponse(res, json_dumps_params={'ensure_ascii': False})


def login(request):
    res, meta = {}, {}
    code = request.GET.get('code')
    NickName = request.GET.get('nickName')
    AvatarUrl = request.GET.get('avatarUrl')
    data = wxAPI().getsession(code)
    # wxuser.objects.update(nickname=user['nickname'], arvatar=user['avatarUrl'], openid=data['openid'], session_key=data['session_key'])
    isin = wxuser.objects.filter(openid=data['openid']).exists()
    if isin:
        wxuser.objects.filter(openid=data['openid']).update(nickname=NickName, arvatar=AvatarUrl,
                                                            session_key=data['session_key'])
    else:
        wxuser.objects.create(nickname=NickName, arvatar=AvatarUrl, openid=data['openid'],
                              session_key=data['session_key'])
    res['data'] = data
    return JsonResponse(res, json_dumps_params={'ensure_ascii': False})
