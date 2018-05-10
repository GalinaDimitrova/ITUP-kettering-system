# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class LunchMenu(models.Model):
    menu_items = models.ManyToManyField('orders.MenuItem', blank=True, related_name='lunch_menu')

    date_created = models.DateTimeField(auto_now_add=timezone.now, null=True)
    last_update = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=True)
