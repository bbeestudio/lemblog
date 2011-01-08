# -*- coding:utf-8 -*-
from django.contrib import admin
from django.shortcuts import get_object_or_404
from django.utils.encoding import smart_str
from models import Cat, Post, Tag, Comment
from django.core.context_processors import request

class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date','published')
    prepopulated_fields = {'slug': ('title',)}

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.tags = obj.tags.lower()
        obj.save()
        obj.tags_list.clear()
        list = [k.strip() for k in obj.tags.split(',')]
        for t in list:
                tag = Tag.objects.filter(title=t)
                if not tag:
                    tag = Tag()
                    tag.title = t
                    tag.save()
                    obj.tags_list.add(tag)
                else:
                    obj.tags_list.add(tag[0])
        obj.save()

    def queryset(self, request):
        qs = super(PostsAdmin, self).queryset(request)
        return qs.filter(user=request.user)

admin.site.register(Post, PostsAdmin)


class CatsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Cat, CatsAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author','text')

admin.site.register(Comment, CommentAdmin)
