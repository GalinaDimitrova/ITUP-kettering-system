from django.db import models


class Office(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=64, blank=True)
    base_menu = models.ForeignKey('orders.BaseMenu', on_delete=models.SET_NULL, blank=True, null=True, default=None, related_name='office')
