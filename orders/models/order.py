# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils import timezone


class Order(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='user_orders')
    menu_items = models.ManyToManyField('orders.MenuItem', related_name='item_orders')
    lunch_menu_id = models.IntegerField()  # Think for better relation with the Lunch menu

    date_created = models.DateTimeField(auto_now_add=timezone.now, null=True)
    last_update = models.DateTimeField(auto_now=True, null=True)
