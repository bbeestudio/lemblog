# -*- coding:utf-8 -*-
from django.template import Library, Node
register = Library()

from blog.plugins.menu.models import ItemMenu

@register.inclusion_tag('blog/plugins/menu.html')
def get_menu():
    return { 'item_menu_list' : ItemMenu.objects.filter(enable=True) }
