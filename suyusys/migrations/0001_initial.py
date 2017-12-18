# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-05 17:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DbServersRedis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=30)),
                ('port', models.CharField(max_length=10)),
                ('monitor', models.IntegerField(blank=True, null=True)),
                ('tags', models.CharField(blank=True, max_length=50, null=True)),
                ('role', models.CharField(max_length=255)),
                ('alive', models.BooleanField(default=False)),
                ('connected', models.CharField(default=0, max_length=255)),
            ],
        ),
    ]