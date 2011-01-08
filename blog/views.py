# -*- coding:utf-8 -*-
from blog.models import Settings
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.contrib.sites.models import Site

from django.conf import settings
from django.contrib.sites.models import Site

def set_headers(request):
    if Settings.objects.all().count()!=0:
        s = Settings.objects.all()[0]
        return {
            'BLOGNAME': s.blogname,
            'META_DESC': s.metad,
            'META_KEYWORDS': s.metak,
            'COPYRIGHTS' : s.copyrights,
			'SITE_NAME' : 'http://' + Site.objects.get(id=settings.SITE_ID).domain + '/'
        }
    else:
        return { 'BLOGNAME':'lemblog', 'META_DESC':'', 'META_KEYWORDS':'', 'COPYRIGHTS':''}
