from django.db import models
from .storage import ImageStorage


# Create your models here.
class user(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, verbose_name='用户名', unique=True)
    avatar = models.ImageField(upload_to='avatar', max_length=200, verbose_name='用户头像', storage=ImageStorage())
    email = models.CharField(max_length=100, verbose_name='邮箱')
    password = models.CharField(max_length=100, verbose_name='密码')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='最后登录时间')
    is_login = models.BooleanField(default=False, verbose_name='是否在登录')
    token = models.CharField(max_length=125, verbose_name='token')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
