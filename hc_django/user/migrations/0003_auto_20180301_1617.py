# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-01 08:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20180301_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_sex',
            field=models.BooleanField(choices=[(0, '男'), (1, '女')], default=0),
        ),
    ]
