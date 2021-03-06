# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-14 12:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Checks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_info', models.IntegerField()),
                ('check_id', models.CharField(max_length=1024)),
                ('check_note', models.CharField(max_length=102400)),
            ],
        ),
        migrations.CreateModel(
            name='CheckStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_status', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='CheckType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=10240)),
            ],
        ),
        migrations.CreateModel(
            name='ProcessType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('process_name', models.CharField(max_length=10240)),
                ('process_type', models.CharField(max_length=10240)),
            ],
        ),
        migrations.AddField(
            model_name='checks',
            name='check_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='check.CheckStatus'),
        ),
        migrations.AddField(
            model_name='checks',
            name='check_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='check.CheckType'),
        ),
    ]
