# -*- coding:utf-8 -*-
from django.template import Library, Node
register = Library()

from blog.plugins.counters.models import Counter

@register.inclusion_tag('blog/plugins/counters.html')
def get_counters():
    return { 'counters_list' : Counter.objects.filter(enable=True) }
