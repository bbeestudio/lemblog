# -*- coding:utf-8 -*-
from django.db import models

class SetingsRSS(models.Model):
    title = models.CharField(verbose_name=u'заголовок', max_length=200, blank=True)
    description =  models.CharField(verbose_name=u'описание', max_length=200, blank=True)

    def __unicode__(self):
        return self.title
    
    class Meta:
         verbose_name = 'RSS лента'
         verbose_name_plural = 'RSS лента'


