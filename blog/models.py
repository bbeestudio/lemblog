# -*- coding:utf-8 -*-
from django.db import models

class Settings(	models.Model):
    blogname = models.CharField(verbose_name=u'название блога', max_length=200, blank=True)
    metad = models.CharField(verbose_name=u'описание', max_length=200, blank=True)
    metak = models.CharField(verbose_name=u'ключевые слова', max_length=200, blank=True)
    copyrights = models.TextField(verbose_name=u'копирайты', blank=True)


    ptitle = models.CharField(verbose_name=u'главная страница', max_length=200, blank=True)
    ptpost = models.CharField(verbose_name=u'заголовок поста', max_length=200, blank=True)
    pcat = models.CharField(verbose_name=u'посты по категории', max_length=200, blank=True)
    bpmonth = models.CharField(verbose_name=u'архив, поиск по месяцам', max_length=200, blank=True)
    pyear = models.CharField(verbose_name=u'архив, поиск по годам', max_length=200, blank=True)
    pcatlist = models.CharField(verbose_name=u'список категорий', max_length=200, blank=True)
    puser = models.CharField(verbose_name=u'пользователь', max_length=200, blank=True)
    puposts = models.CharField(verbose_name=u'посты пользователя', max_length=200, blank=True)
    ptaglist = models.CharField(verbose_name=u'посты по тегу', max_length=200, blank=True)
    parch = models.CharField(verbose_name=u'архив', max_length=200, blank=True)

    titledisable = models.CharField(verbose_name=u'заголовок страницы', max_length=200, blank=True)
    textdisable = models.TextField(verbose_name=u'текст сообщения', max_length=200, blank=True)
    disable = models.BooleanField(verbose_name=u'выключить сайт', default=False, blank=True)

    class Meta:
        verbose_name = 'настройки блога'
        verbose_name_plural = 'настройки блога'

    def __unicode__(self):
        return self.blogname
