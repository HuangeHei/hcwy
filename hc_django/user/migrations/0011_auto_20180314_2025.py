# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-14 12:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_auto_20180314_1734'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checks',
            name='check_status',
        ),
        migrations.RemoveField(
            model_name='checks',
            name='check_type',
        ),
        migrations.DeleteModel(
            name='Checks',
        ),
        migrations.DeleteModel(
            name='CheckStatus',
        ),
        migrations.DeleteModel(
            name='CheckType',
        ),
    ]