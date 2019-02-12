# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-11 08:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0014_auto_20190208_0839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asik',
            name='gps',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='lab.Gps'),
        ),
        migrations.AlterField(
            model_name='asik',
            name='owner',
            field=models.CharField(default='admin', max_length=50),
        ),
        migrations.AlterField(
            model_name='gps',
            name='owner',
            field=models.CharField(default='admin', max_length=50),
        ),
        migrations.AlterField(
            model_name='gps',
            name='serial_num',
            field=models.CharField(default='123456', max_length=20),
        ),
    ]
