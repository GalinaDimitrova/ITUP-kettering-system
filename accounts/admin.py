# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib import admin
from django.contrib.auth.models import Permission
# from django.contrib.auth.forms import UserChangeForm

from accounts.models import User, Office


# TODO: Add User form and hide the password. Add Change form that contains only fields 'username', 'password1' and 'password2'
class UserAdmin(admin.ModelAdmin):
    # form = UserChangeForm
    fieldsets = (
        (None, {'fields': ('uid', 'username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'office')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    filter_horizontal = ['user_permissions', 'groups']
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'office')
    ordering = ('username',)
    raw_id_fields = ()

admin.site.register(User, UserAdmin)


class OfficeForm(forms.ModelForm):
    class Meta:
        model = Office
        fields = '__all__'
        widgets = {
            'address': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }


class OfficeAdmin(admin.ModelAdmin):
    form = OfficeForm
admin.site.register(Office, OfficeAdmin)


class PermissionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Permission, PermissionAdmin)
