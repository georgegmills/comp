# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-22 21:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='representative',
            name='first_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='representative',
            name='last_name',
            field=models.CharField(default='', max_length=200),
        ),
    ]