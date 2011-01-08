# -*- coding:utf-8 -*-
from django.contrib import admin
from models import TwitterAcc

from django.contrib.sites.models import Site
from django.conf import settings

class TwitterAccAdmin(admin.ModelAdmin):
    list_display = ('name','enable',)
    add_form_template = 'blog/plugins/twitter/add_form.html'

    def add_view(self, request, form_url='', extra_context=None):
        current_site = Site.objects.get(id=settings.SITE_ID)
        url = 'http://' + current_site.domain + '/twitter/auth'
        my_context = {
            'url': url,
        }
        return super(TwitterAccAdmin, self).add_view(request, form_url,
            extra_context=my_context)

admin.site.register(TwitterAcc, TwitterAccAdmin)