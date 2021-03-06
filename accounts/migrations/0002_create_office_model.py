# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-10 13:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('phone', models.CharField(blank=True, max_length=64)),
                ('base_menu', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='office', to='orders.BaseMenu')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='office',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Office'),
        ),
    ]
