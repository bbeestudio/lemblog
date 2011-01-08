# -*- coding:utf-8 -*-
from blog.plugins.custom_user.models import CustomUser
from django.shortcuts import get_object_or_404
from blog.core.models import Post
from django.template import Library, Node

register = Library()

@register.inclusion_tag('blog/plugins/custom_user/templatetags/posts_by_user.html')
def posts_by_user(name, count):
    user = get_object_or_404(CustomUser, username=name)
    posts_list = Post.objects.filter(user=user.id).order_by('-pub_date')[:count]
    return { 'user':name, 'posts_list':posts_list }
