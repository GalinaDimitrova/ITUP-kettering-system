# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib import admin

from orders.models import BaseMenu, LunchMenu, Comment, Order, MenuItem


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 7}),
        }


class ManuItemsInline(admin.StackedInline):
    model = MenuItem
    form = MenuItemForm


class BaseMenuAdmin(admin.ModelAdmin):
    inlines = [
        ManuItemsInline,
    ]
admin.site.register(BaseMenu, BaseMenuAdmin)


class LunchMenuAdmin(admin.ModelAdmin):
    filter_horizontal = ['menu_items']
admin.site.register(LunchMenu, LunchMenuAdmin)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80, 'rows': 7}),
        }


class CommentAdmin(admin.ModelAdmin):
    form = CommentForm
    raw_id_fields = ('user', 'menu_item')

admin.site.register(Comment, CommentAdmin)


class OrderAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)
    filter_horizontal = ['menu_items']
admin.site.register(Order, OrderAdmin)


class MenuItemAdmin(admin.ModelAdmin):
    form = MenuItemForm
admin.site.register(MenuItem, MenuItemAdmin)
