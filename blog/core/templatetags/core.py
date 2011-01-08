# -*- coding:utf-8 -*-
from django.template import Library, Node, Variable
from django import template
register = Library()

from blog.core.models import Cat, Post

class CountNode(Node):

    def __init__(self, tag_name, field, values):
        self.tag_name = tag_name
        self.field = field
        self.args = [] 
        for val in values:
            self.args.append(Variable(val))     

    def render(self, context):
        values = []
        for arg in self.args:
            values.append(arg.resolve(context))
        count = ''
        if len(values)==1:
            if self.field == "category":
                count = Post.objects.filter(published=True, cat=values[0]).count()
            if self.field == "arch_year":
                count = Post.objects.filter(published=True, pub_date__year=values[0]).count()
            if count=='':
                raise template.TemplateSyntaxError, "%r tag had invalid arguments" % self.tag_name

        if len(values)==2:
            if self.field == "arch_year_month":
                count = Post.objects.filter(published=True, pub_date__year=values[0], pub_date__month=values[1]).count()
            if count=='':
                raise template.TemplateSyntaxError, "%r tag had invalid arguments" % self.tag_name
        return count


def let_count(parser, token):
    values  = token.split_contents()
    tag_name = values[0]
    field = values[1]
    values = values[2:]
    if len(values)>2:
        raise template.TemplateSyntaxError, "%r tag requires no more two arguments" % token.contents.split()[0]
    if len(values)==0:
        raise template.TemplateSyntaxError, "%r tag requires arguments" % token.contents.split()[0]
    return CountNode(tag_name, field, values)

register.tag('count', let_count)


@register.inclusion_tag('blog/core/templatetags/cats_list.html')
def get_cats_list():
    return { 'cats_list':Cat.objects.all() }

	
@register.inclusion_tag('blog/core/templatetags/arch.html')
def get_arch():
    years = {}
    for date in Post.objects.dates('pub_date', 'year'):
        years[date.year] = Post.objects.filter(pub_date__year=date.year).dates('pub_date', 'month')
    return { 'years':years }


