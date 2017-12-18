# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-05 17:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suyusys', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dbserversredis',
            options={'verbose_name': 'redis\u76d1\u63a7\u673a\u7ec4', 'verbose_name_plural': '\u76d1\u63a7\u4e3b\u673a'},
        ),
        migrations.RemoveField(
            model_name='dbserversredis',
            name='host',
        ),
        migrations.AddField(
            model_name='dbserversredis',
            name='hostip',
            field=models.GenericIPAddressField(default='0.0.0.0'),
        ),
    ]
