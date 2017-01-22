# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-22 21:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Representative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('BOR', 'BOR AE'), ('HRONE', 'HR One AE'), ('NGE', 'NGE AE'), ('SDR', 'SDR'), ('CLIENT', 'Client AE')], default='HRONE', max_length=6)),
                ('quota', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('variable', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('base', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
            ],
        ),
    ]
