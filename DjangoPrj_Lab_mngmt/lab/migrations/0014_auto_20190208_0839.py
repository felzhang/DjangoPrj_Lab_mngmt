# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-08 08:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0013_auto_20190208_0758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asik',
            name='gps_id',
        ),
        migrations.AddField(
            model_name='asik',
            name='gps',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='lab.Gps'),
        ),
        migrations.AlterField(
            model_name='asik',
            name='eth_ip',
            field=models.GenericIPAddressField(default='10.0.0.0', unique=True),
        ),
        migrations.AlterField(
            model_name='asik',
            name='serial_num',
            field=models.CharField(default='123456', max_length=50, unique=True),
        ),
    ]