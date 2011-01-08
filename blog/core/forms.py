# -*- coding:utf-8 -*-
from django import forms
from django.core import validators

class CommentForm(forms.Form):
    author = forms.CharField(label='автор', widget=forms.TextInput(attrs={'size':'16'}), error_messages={'invalid': (u'Некорректный пользователь'), 'required':(u'Вы не ввели имя')})
    text = forms.CharField(label='комментарий', widget=forms.Textarea(attrs={'rows':4, 'cols':60}), error_messages={'invalid': (u'Некорректный комментарий'), 'required':(u'Вы не ввели комментарий')})
    url = forms.CharField(label='сайт', widget=forms.TextInput(attrs={'size':'16'}), error_messages={'invalid': (u'Некорректный адрес')}, required=False)

