# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-30 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suyu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='filepath',
            field=models.FilePathField(default='F:\\django_test\\media', max_length=255, verbose_name='\u6587\u4ef6\u76ee\u5f55'),
        ),
    ]
