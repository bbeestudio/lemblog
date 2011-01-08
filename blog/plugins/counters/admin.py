# -*- coding:utf-8 -*-
from django.contrib import admin

from models import Counter

class CounterAdmin(admin.ModelAdmin):
    list_display = ('name','enable')

admin.site.register(Counter, CounterAdmin)
