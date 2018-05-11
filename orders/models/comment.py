# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils import timezone


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='comments', null=True)
    menu_item = models.ForeignKey('orders.MenuItem', on_delete=models.SET_NULL, null=True, related_name='comments')

    rate = models.DecimalField(max_digits=3, decimal_places=2, default=0)  # TODO: add validator for min_value=0, max_value=5,
    text = models.CharField(max_length=255, blank=True)
    date_created = models.DateTimeField(auto_now_add=timezone.now, null=True)
