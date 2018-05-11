# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class MenuItem(models.Model):
    SOUP = 'soup'
    SALAD = 'salad'
    DESERT = 'desert'
    MEAL = 'meal'
    VEGETARIAN = 'vegetarian'
    OTHER = 'other'
    ITEM_TYPES_CHOICES = (
        (SOUP, 'Soup'),
        (SALAD, 'Salad'),
        (DESERT, 'Desert'),
        (MEAL, 'meal'),
        (VEGETARIAN, 'Vegetarian'),
        (OTHER, 'Other'),
    )

    base_menu = models.ForeignKey('orders.BaseMenu', on_delete=models.PROTECT, blank=True, null=True, default=None, related_name='menu_items')

    item_type = models.CharField(max_length=20, choices=ITEM_TYPES_CHOICES, default=OTHER)
    name = models.CharField(max_length=120, blank=True)
    description = models.CharField(max_length=255, blank=True)
    rate = models.DecimalField(max_digits=3, decimal_places=2, default=0)  # TODO: add validator for min_value=0, max_value=5,
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # TODO: add validator for min_value=0
    # image = models.ImageField()  # TODO: add restrictions to that field
    date_created = models.DateTimeField(auto_now_add=timezone.now, null=True)
    last_update = models.DateTimeField(auto_now=True, null=True)
