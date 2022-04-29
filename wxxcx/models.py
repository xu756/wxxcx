from django.db import models
from wxxcx.methods.storage import ImageStorage


# 小程序配置
class WxxcConfig(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='主键')
    key = models.CharField(max_length=50, verbose_name='配置键')
    value = models.CharField(max_length=128, verbose_name='配置值')
    last_update_time = models.DateTimeField(auto_now=True, verbose_name='最后修改时间')

    class Meta:
        verbose_name = '小程序配置'
        verbose_name_plural = verbose_name


# 轮播图
class swiper(models.Model):
    id = models.AutoField(verbose_name="轮播图id", primary_key=True)
    img = models.ImageField(verbose_name="轮播图", upload_to="banner", storage=ImageStorage())
    name = models.CharField(verbose_name="轮播图名称", max_length=32)
    time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name


# 通知
class notice(models.Model):
    id = models.AutoField(verbose_name="通知id", primary_key=True)
    title = models.CharField(verbose_name="通知标题", max_length=32)
    content = models.TextField(verbose_name="通知内容", blank=True, null=True)
    time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    class Meta:
        verbose_name = "通知"
        verbose_name_plural = verbose_name


# 专题栏目
class column(models.Model):
    name = models.CharField(verbose_name="专题栏目名称", max_length=32, unique=True)
    path = models.CharField(verbose_name="专题栏目路径", max_length=32)
    time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    img = models.ImageField(verbose_name="专题栏目图片", upload_to="column", storage=ImageStorage())

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "专题栏目"
        verbose_name_plural = verbose_name


# 文章
class article(models.Model):
    id = models.AutoField(verbose_name="文章id", primary_key=True)
    title = models.CharField(verbose_name="文章标题", max_length=32)
    content = models.TextField(verbose_name="文章内容", blank=True, null=True)
    time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    column = models.ForeignKey(column, verbose_name="文章所属专题栏目", on_delete=models.CASCADE, to_field="name")

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name


# 微信用户
class wxuser(models.Model):
    id = models.AutoField(verbose_name="用户id", primary_key=True)
    openid = models.CharField(verbose_name="用户openid", max_length=128)
    nickname = models.CharField(verbose_name="用户昵称", max_length=64)
    arvatar = models.CharField(verbose_name="用户头像", max_length=256)
    session_key = models.CharField(verbose_name="会话密钥", max_length=128)
    time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    last_time = models.DateTimeField(verbose_name="最后登录时间", auto_now=True)

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name


# 留言
class message(models.Model):
    id = models.AutoField(verbose_name="id", primary_key=True)
    user_id = models.CharField(verbose_name="留言用户openid", max_length=128, db_column="message_user_id")
    content = models.CharField(verbose_name="留言内容", max_length=256)
    img = models.CharField(verbose_name="留言图片(列表)", max_length=256)
    time = models.DateTimeField(verbose_name="留言时间", auto_now_add=True)
    is_reply = models.BooleanField(verbose_name="是否回复", default=False)
    is_show = models.BooleanField(verbose_name="是否显示", default=True)
    # 回复内容
    reply = models.CharField(verbose_name="回复内容", max_length=256, null=True, blank=True)
    reply_time = models.DateTimeField(verbose_name="回复时间", null=True, blank=True)

    class Meta:
        verbose_name = "留言"
        verbose_name_plural = verbose_name


# 储存留言图片
class message_img(models.Model):
    id = models.AutoField(verbose_name="id", primary_key=True)
    message_id = models.CharField(verbose_name="留言id", max_length=128)
    img = models.ImageField(verbose_name="留言图片", upload_to="message", storage=ImageStorage())

    class Meta:
        verbose_name = "留言图片"
        verbose_name_plural = verbose_name
