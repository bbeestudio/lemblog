# -*- coding:utf-8 -*-
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext, Template,  Context
from blog.core.views import paginate

from models import CustomUser
from blog.core.models import Post
from blog.models import Settings
from blog.core.views import render_template

def user(request,name):
    if Settings.objects.all()[0]:
        s = Settings.objects.all()[0]
        title = render_template(s.puser, AUTHORNAME=name)
    else:
        title = u'Пользователь ' + name
    user = get_object_or_404(CustomUser, username=name)
    return render_to_response('blog/plugins/custom_user/user.html', {'title' : title, 'user': user, 'name':name}, context_instance=RequestContext(request))

def get_user_posts(request,name):
    user = get_object_or_404(CustomUser, username=name)
    if Settings.objects.all()[0]:
        s = Settings.objects.all()[0]
        title = render_template(s.puposts, AUTHORNAME=name)
    else:
        title = u'Посты пользователя' + name
    posts_list =  paginate(request,Post.objects.filter(user=user.id).order_by('-pub_date'),10)
    return render_to_response('blog/core/posts_list.html', {'title': title, 'posts_list': posts_list}, context_instance=RequestContext(request))
