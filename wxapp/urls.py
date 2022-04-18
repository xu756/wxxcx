from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from wxxxc import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  url('admin/', admin.site.urls),
                  path('', views.index, name='模板样例'),
                  path('getswiper/', views.getswiper, name='获取轮播图'),
                  path('api/login/', views.login, name='登录'),
                  path('vue/', include('vueqd.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
