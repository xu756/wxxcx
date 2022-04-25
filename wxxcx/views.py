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
    wxAPI().getAccess_token()
    return render(request, 'index.html', a)


@cache_page(60)
def getdefault(request):
    res, meta = {}, {}
    res['swiper'] = list(swiper.objects.all().values())[:3]
    res['notice'] = notice.objects.values('id', 'title').last()
    return JsonResponse(res, json_dumps_params={'ensure_ascii': False})


def login(request):
    res, meta = {}, {}
    code = request.GET.get('code')
    NickName = request.GET.get('nickName')
    AvatarUrl = request.GET.get('avatarUrl')
    data = wxAPI().getsession(code)
    isin = wxuser.objects.filter(openid=data['openid']).exists()
    if isin:
        wxuser.objects.filter(openid=data['openid']).update(nickname=NickName, arvatar=AvatarUrl,
                                                            session_key=data['session_key'])
    else:
        wxuser.objects.create(nickname=NickName, arvatar=AvatarUrl, openid=data['openid'],
                              session_key=data['session_key'])
    res['data'] = data
    return JsonResponse(res, json_dumps_params={'ensure_ascii': False})


# 意见反馈
def feedback(request):
    res, meta = {}, {}
    file = request.FILES.getlist('file')
    print(file)
    print(request.POST.get('userfk'))
    res['res'] = 'ok'
    return JsonResponse(res, json_dumps_params={'ensure_ascii': False})
