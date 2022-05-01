from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from wxxcx import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  url('admin/', admin.site.urls),
                  path('', views.index, name='模板样例'),
                  path('vue/', include('vueqd.urls')),
                  path('wxxcx/', include('wxxcx.urls')),
                  url(r'^ckeditor/', include('ckeditor_uploader.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
