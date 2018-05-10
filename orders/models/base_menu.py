# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class BaseMenu(models.Model):
    distributor_info = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=timezone.now, null=True)
    last_update = models.DateTimeField(auto_now=True, null=True)
