# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-01 19:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20170401_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='timezone',
            field=models.CharField(default=django.utils.timezone.now, max_length=40),
            preserve_default=False,
        ),
    ]
