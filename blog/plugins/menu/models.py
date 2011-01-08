# -*- coding:utf-8 -*-
from django.db import models

class ItemMenu(models.Model):
    name = models.CharField(verbose_name=u'название', max_length=200)
    target = models.CharField(verbose_name=u'ссылка', max_length=200)
    enable = models.BooleanField(verbose_name=u'отображать')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'меню блога'
        verbose_name_plural = 'меню блога'
