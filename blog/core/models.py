# -*- coding:utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

class Cat(models.Model):
    title = models.CharField(verbose_name=u'название',max_length=200)
    slug = models.SlugField(verbose_name=u'cсылка', unique=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'рубрика'
        verbose_name_plural = 'рубрики'

    @models.permalink
    def get_absolute_url(self):
        return ('cat', [str(self.slug)])


class Tag(models.Model):
    title = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(verbose_name=u'заголовок', max_length=200)
    slug = models.SlugField(verbose_name=u'ссылка', unique=True)
    cat = models.ForeignKey('Cat',verbose_name=u'рубрика')
    desc = models.TextField(verbose_name=u'вступление')
    text = models.TextField(verbose_name=u'полный текст записи')
    user   = models.ForeignKey(User, editable=False)
    pub_date = models.DateField(verbose_name=u'Дата публикации',default=datetime.now)
    pub_time = models.TimeField(verbose_name=u'Время публикации', default=datetime.now, editable=False)
    tags = models.CharField(verbose_name=u'метки',max_length=200)
    tags_list = models.ManyToManyField(Tag, editable=False)
    tweeted = models.BooleanField(default=False, editable=False)
    published = models.BooleanField(verbose_name=u'опубликовать',default=False)


    class Meta:
        ordering = ('-pub_date', '-pub_time')
        verbose_name = 'запись'
        verbose_name_plural = 'записи'

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('post', [str(self.slug)])


class Comment(models.Model):
    author = models.CharField(verbose_name=u'автор', max_length=200)
    text = models.CharField(verbose_name=u'текст', max_length=200)
    url = models.CharField(verbose_name=u'сайт', blank=True, max_length=200)
    post = models.ForeignKey('Post',verbose_name=u'публикация')
    pub_date = models.DateField(verbose_name=u'дата публикации', default=datetime.now)
    pub_time = models.TimeField(verbose_name=u'время публикации', default=datetime.now)
    
    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'комментарий'
        verbose_name_plural = 'коммментарии'

    def __unicode__(self):
        return self.text
