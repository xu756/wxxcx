from django.contrib import admin
from .models import *


# Register your models here.
class userAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_login','updated_at')


admin.site.register(user, userAdmin)
