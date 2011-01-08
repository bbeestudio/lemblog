# -*- coding:utf-8 -*-
from django.core.paginator import Paginator, InvalidPage, EmptyPage 
from django.db.models.signals import post_save
from django.shortcuts import get_object_or_404, render_to_response, HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.template import RequestContext, Template,  Context

from django.contrib.sites.models import Site
from django.conf import settings
import httplib, urllib, urllib2

from blog.models import Settings
from blog.core.models import Cat, Post, Tag, Comment
from blog.plugins.twitter.models import TwitterAcc
from blog.plugins.twitter.views import *
from blog.core.forms import CommentForm

def index(request):
    posts_list=paginate(request, Post.objects.all(), 7)
    if Settings.objects.all()[0]:
        s = Settings.objects.all()[0]
        title = render_template(s.ptitle, BLOGNAME=s.blogname)
    else:
        title = 'Главная'
    return render_to_response('blog/core/posts_list.html', {'title': title, 'posts_list': posts_list}, context_instance=RequestContext(request))
    
def maintenance(request):
    if Settings.objects.all()[0]:
        s = Settings.objects.all()[0]
        text = render_template(s.textdisable, BLOGNAME=s.blogname)
        title = render_template(s.titledisable, BLOGNAME=s.blogname)
    else:
        title = 'Сайт временно недоступен'
        text = 'Извините, сайт временно недоступен'
    return render_to_response('blog/maintenance.html', { 'title':title, 'text': text })

def detail(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)

    if Settings.objects.all()[0]:
        s = Settings.objects.all()[0]
        title = render_template(s.ptpost, BLOGNAME=s.blogname, CATNAME=post.cat.title, POSTNAME=post.title)
    else:
        title = post.title

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            c = Comment(author=form.cleaned_data['author'], text=form.cleaned_data['text'], post=post, url=form.cleaned_data['url']).save()
            return HttpResponseRedirect(reverse('blog.core.views.detail', args=[post_slug]))
        else:
            errors = form.errors
    else:
        errors = {}
    comment_list = Comment.objects.filter(post=post.id).order_by('pub_date','pub_time')
    return render_to_response('blog/core/detail.html', {'title':title, 'post':post, 'form':form, 'errors':errors, 'comment_list':comment_list}, context_instance=RequestContext(request))

def cats(request, cat_slug=None):
    if cat_slug:
        cat = get_object_or_404(Cat, slug=cat_slug)
        posts_list = paginate(request,Post.objects.filter(cat=cat.id),7)
        if Settings.objects.all()[0]:
            s = Settings.objects.all()[0]
            title = render_template(s.pcat, BLOGNAME=s.blogname, CATNAME = cat.title)
        else:
            title = cat.title
        return render_to_response('blog/core/posts_list.html', {'title': title, 'posts_list': posts_list}, context_instance=RequestContext(request))
    else:
        cats_list = paginate(request,Cat.objects.all(),10)
        if Settings.objects.all()[0]:
            s = Settings.objects.all()[0]
            title = render_template(s.pcatlist, BLOGNAME=s.blogname)
        else:
            title = 'Список категорий'
        return render_to_response('blog/core/cats_list.html', {'title':title, 'cats_list': cats_list}, context_instance=RequestContext(request))


def tags(request, tags_name):
    tag = get_object_or_404(Tag, title=tags_name.lower())
    posts_list=paginate(request,Post.objects.filter(tags__contains=tag.title),7)
    if Settings.objects.all()[0]:
        s = Settings.objects.all()[0]
        title = render_template(s.ptaglist, BLOGNAME=s.blogname, TAGNAME=tag.title)
    else:
        title = 'Поиск по тегам'
    return render_to_response('blog/core/posts_list.html', {'title': title, 'posts_list': posts_list}, context_instance=RequestContext(request))


def arch(request, year_id=0, month_id=0):

    if month_id == 0:
        posts_list = paginate(request,Post.objects.filter(pub_date__year=year_id),7)
        if Settings.objects.all()[0]:
            s = Settings.objects.all()[0]
            title = render_template(s.pyear, BLOGNAME=s.blogname, ARCHYEAR = year_id)
        else:
            title = 'Архив, поиск по годам'
    else:
        posts_list = paginate(request,Post.objects.filter(pub_date__year=year_id, pub_date__month=month_id),7)
        if Settings.objects.all()[0]:
            s = Settings.objects.all()[0]
            p = Post.objects.filter(pub_date__year=year_id, pub_date__month=month_id)[0]
            title = render_template(s.bpmonth.replace('ARCHMONTH', 'ARCHMONTH|date:"F"'), BLOGNAME=s.blogname, ARCHYEAR=p.pub_date.year, ARCHMONTH=p.pub_date)
        else:
            title = 'Архив, поиск по месяцам'
    

    if posts_list.object_list:
	return render_to_response('blog/core/posts_list.html', {'title': title, 'posts_list': posts_list }, context_instance=RequestContext(request))
    else:    
        dates = Post.objects.dates('pub_date', 'month')
        if Settings.objects.all()[0]:
            s = Settings.objects.all()[0]
            title = render_template(s.parch, BLOGNAME=s.blogname)
        else:
            title = 'Архив'
        return render_to_response('blog/core/arch.html', {'dates':dates, 'title':title }, context_instance=RequestContext(request))


def paginate(request, list, num):
    paginator = Paginator(list, num)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        paginate_list = paginator.page(page)
    except (EmptyPage, InvalidPage):
        paginate_list = paginator.page(paginator.num_pages)

    return paginate_list

def render_template(title, **kwards):
    t = Template(title)
    c = Context(kwards)
    return t.render(c)

def post_to_twitter(sender,instance,**kwargs):
        if instance.published and not instance.tweeted:
                try:
                    current_site = Site.objects.get(id=settings.SITE_ID)
	            long_url = 'http://' + current_site.domain + instance.get_absolute_url()
                    short_url = ShortUrl(long_url)
                    twit = short_url + " " + instance.title
                    twitit(twit)
                    instance.tweeted = True
                    instance.save()
                except: 
                    return HttpResponse("Something is going wrong")


post_save.connect(post_to_twitter, sender=Post)
