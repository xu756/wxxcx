from django.contrib import admin
from .models import *


class WxxcConfigAdmin(admin.ModelAdmin):
    # 设置显示的字段
    list_display = ('key', 'value', 'last_update_time')
    # 不可以修改的字段
    # 排序
    ordering = ('id',)
    readonly_fields = ('key',)


admin.site.register(WxxcConfig, WxxcConfigAdmin)


class swiperAdmin(admin.ModelAdmin):
    list_display = ('id', 'img', 'name')


admin.site.register(swiper, swiperAdmin)


class wxuserAdmin(admin.ModelAdmin):
    list_display = ('id', 'nickname', 'time', 'last_time')


admin.site.register(wxuser, wxuserAdmin)


class messageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'content', 'time')


admin.site.register(message, messageAdmin)


class noticeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time')


admin.site.register(notice, noticeAdmin)


class columnAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'path', 'time', 'img')


admin.site.register(column, columnAdmin)


class articleAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'time','img' ,'column')
    search_fields = ('title', 'content')


admin.site.register(article, articleAdmin)
