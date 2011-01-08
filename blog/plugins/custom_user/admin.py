# -*- coding:utf-8 -*-

from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AdminPasswordChangeForm
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.auth.models import Group
import Image
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser        

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'last_name', 'first_name')
    list_filter = ()
    filter = ()
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'desc', 'vkontakte', 'sait', 'icq', 'skype', 'MSN', 'flickr', 'jabber', 'gtalk', 'twitter', 'facebook', 'image')}),
    )

    def save_model(self, request, obj, form, change):   
        obj.is_staff = True
        obj.is_superuser = True
        obj.save()
        if obj.image:
            path = obj.image.path
            image = Image.open(path)
            image = image.resize((128, 128), Image.ANTIALIAS)
            image.save(path)

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(CustomUser, CustomUserAdmin)

