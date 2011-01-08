# -*- coding:utf-8 -*-
from django.db import models

class TwitterAcc(models.Model):
    name = models.CharField(verbose_name=u'название',max_length=200)
    PIN = models.CharField(verbose_name=u'PIN',max_length=200, editable=False)
    enable = models.BooleanField(verbose_name=u'транслировать')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'трансляция записей в Твиттер'
        verbose_name_plural = 'трансляция записей в Твиттер'