# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-20 18:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suyu', '0005_auto_20171120_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='runmodel',
            name='modelid',
            field=models.CharField(default=0, max_length=10, verbose_name='\u6a21\u5757ID'),
        ),
    ]