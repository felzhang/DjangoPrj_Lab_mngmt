# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-31 01:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0002_auto_20190131_0146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asik',
            name='test_column',
        ),
    ]
