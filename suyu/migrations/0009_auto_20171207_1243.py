# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-07 12:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suyu', '0008_redisinfo_autotime'),
    ]

    operations = [
        migrations.RenameField(
            model_name='redisinfo',
            old_name='autoTime',
            new_name='redisTime',
        ),
    ]
