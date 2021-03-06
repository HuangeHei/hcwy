# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-19 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChildItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Index', models.CharField(max_length=100)),
                ('Name', models.CharField(default='无名称设置名称', max_length=1024)),
                ('To', models.CharField(default='#409EFF', max_length=1024)),
                ('Icon', models.CharField(default='None', max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='SidaItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Index', models.CharField(max_length=100)),
                ('Name', models.CharField(default='无名称设置名称', max_length=1024)),
                ('Icon', models.CharField(default='None', max_length=1024)),
                ('Child', models.ManyToManyField(to='index.ChildItem')),
            ],
        ),
    ]
