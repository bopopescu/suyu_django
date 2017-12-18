# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-30 18:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('saltstack', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Minions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minion', models.CharField(max_length=50, unique=True, verbose_name='\u5ba2\u6237\u7aef')),
                ('status', models.CharField(choices=[('Accepted', 'Accepted'), ('Unaccepted', 'Unaccepted'), ('Rejected', 'Rejected')], default='Unknown', max_length=20, verbose_name='Key\u72b6\u6001')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('saltserver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saltstack.saltserver', verbose_name='\u6240\u5c5eSalt\u670d\u52a1\u5668')),
            ],
            options={
                'verbose_name': 'Salt\u5ba2\u6237\u7aef',
                'verbose_name_plural': 'Salt\u5ba2\u6237\u7aef\u5217\u8868',
            },
        ),
    ]