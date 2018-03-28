# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-01 09:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20180301_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='adduser',
            name='user_desc',
            field=models.CharField(default=1, max_length=102400),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='user_baoxian',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.UserBaoXian'),
        ),
    ]
