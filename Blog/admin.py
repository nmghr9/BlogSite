from django.contrib import admin
from .models import *


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'createTime', 'updateTime']

    class Meta:
        __module__ = Blog


admin.site.register(Blog, BlogAdmin)