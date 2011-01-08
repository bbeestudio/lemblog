# -*- coding:utf-8 -*-
from django.contrib import admin

from models import ItemMenu

class ItemMenuAdmin(admin.ModelAdmin):
    list_display = ('name','enable')

admin.site.register(ItemMenu, ItemMenuAdmin)
