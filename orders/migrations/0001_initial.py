# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-10 13:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distributor_info', models.CharField(blank=True, max_length=255, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_update', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LunchMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_update', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_type', models.CharField(choices=[('soup', 'Soup'), ('salad', 'Salad'), ('desert', 'Desert'), ('meal', 'meal'), ('vegetarian', 'Vegetarian'), ('other', 'Other')], default='other', max_length=20)),
                ('name', models.CharField(blank=True, max_length=120)),
                ('address', models.CharField(blank=True, max_length=120)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('rate', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_update', models.DateTimeField(auto_now=True, null=True)),
                ('base_menu', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='menu_items', to='orders.BaseMenu')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lunch_menu_id', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_update', models.DateTimeField(auto_now=True, null=True)),
                ('menu_items', models.ManyToManyField(related_name='item_orders', to='orders.MenuItem')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='lunchmenu',
            name='menu_items',
            field=models.ManyToManyField(blank=True, related_name='lunch_menu', to='orders.MenuItem'),
        ),
        migrations.AddField(
            model_name='comment',
            name='menu_item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to='orders.MenuItem'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
