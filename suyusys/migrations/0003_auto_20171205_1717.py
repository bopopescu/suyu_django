# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-05 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suyusys', '0002_auto_20171205_1708'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dbserversredis',
            options={'verbose_name': '\u76d1\u63a7\u4e3b\u673a', 'verbose_name_plural': 'redis\u76d1\u63a7\u673a\u7ec4'},
        ),
        migrations.AlterField(
            model_name='dbserversredis',
            name='alive',
            field=models.BooleanField(default=False, verbose_name='alive'),
        ),
        migrations.AlterField(
            model_name='dbserversredis',
            name='connected',
            field=models.CharField(default=0, max_length=255, verbose_name='\u8fde\u63a5\u6570'),
        ),
        migrations.AlterField(
            model_name='dbserversredis',
            name='hostip',
            field=models.GenericIPAddressField(default='0.0.0.0', verbose_name='\u4e3b\u673aIP'),
        ),
        migrations.AlterField(
            model_name='dbserversredis',
            name='monitor',
            field=models.CharField(choices=[('Ture', 'ON'), ('False', 'OFF')], default='Ture', max_length=30, null=True, verbose_name='\u662f\u5426\u5f00\u542f\u76d1\u63a7'),
        ),
        migrations.AlterField(
            model_name='dbserversredis',
            name='port',
            field=models.CharField(max_length=10, verbose_name='\u7aef\u53e3'),
        ),
        migrations.AlterField(
            model_name='dbserversredis',
            name='role',
            field=models.CharField(max_length=255, verbose_name='\u89d2\u8272'),
        ),
    ]
