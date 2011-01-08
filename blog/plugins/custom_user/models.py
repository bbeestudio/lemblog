# -*- coding:utf-8 -*-
from django.contrib.auth.models import User, UserManager
from django.db import models

from blog.core.models import Post

class CustomUser(User):
    desc = models.TextField(verbose_name=u'описание', blank=True)
    sait =  models.CharField(verbose_name=u'личный сайт', max_length=200, blank=True)
    icq = models.CharField(verbose_name=u'ICQ', max_length=200, blank=True)
    skype = models.CharField(max_length=200, blank=True)
    MSN = models.CharField(max_length=200, blank=True)
    flickr = models.CharField(max_length=200, blank=True)
    jabber = models.CharField(max_length=200, blank=True)
    gtalk = models.CharField(verbose_name=u'GTalk', max_length=200, blank=True)
    twitter = models.CharField(max_length=200, blank=True)
    facebook = models.CharField(max_length=200, blank=True)
    vkontakte = models.CharField(verbose_name=u'ВКонтакте', max_length=200, blank=True)
    image = models.ImageField(verbose_name=u'Аватар', upload_to='users', blank=True)    
    objects = UserManager()

    class Meta:
         verbose_name = 'автор'
         verbose_name_plural = 'авторы'


