# -*- coding:utf-8 -*-
from django.db import models

class Counter(models.Model):
    name = models.CharField(verbose_name=u'название',max_length=200)
    code = models.TextField(verbose_name=u'код счетчика')
    enable = models.BooleanField(verbose_name=u'включен')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'счетчик посещений'
        verbose_name_plural = 'счетчики посещений'
