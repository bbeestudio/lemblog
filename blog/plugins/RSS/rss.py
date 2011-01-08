# -*- coding:utf-8 -*-
from django.contrib.syndication.views import Feed
from blog.core.models import Post
from blog.plugins.RSS.models import SetingsRSS
from django.shortcuts import get_object_or_404

class LatestPosts(Feed):

    def items(self):
        return Post.objects.filter(published=True)[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text


    def title(self):
       if SetingsRSS.objects.all().count()!=0:
           return '%s' %  SetingsRSS.objects.all()[0].title

       else:
           return 'my_title'

    link = '/rss/'

    def description(self):
       if SetingsRSS.objects.all().count()!=0:
           return '%s' %  SetingsRSS.objects.all()[0].description
       else:
           return 'my_description'

