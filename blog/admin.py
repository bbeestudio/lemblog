# -*- coding:utf-8 -*-
from django.contrib import admin
from blog.models import Settings

class SettingsAdmin(admin.ModelAdmin):
    list_display = ('blogname', )

    fieldsets = (
        ('Основные настройки', {
            'fields': ('blogname', 'metad', 'metak', 'copyrights')
        }),
        ('Заголовки страниц блога', {
            'fields': ('ptitle', 'pcat', 'bpmonth', 'pyear', 'puser', 'puposts', 'ptpost', 'pcatlist', 'ptaglist', 'parch')
        }),
        ('Технические работы', {
            'fields': ('titledisable', 'textdisable', 'disable')
        }),
    )

admin.site.register(Settings, SettingsAdmin)
