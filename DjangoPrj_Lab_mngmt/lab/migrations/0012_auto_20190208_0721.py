# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-08 07:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0011_auto_20190131_0328'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_num', models.CharField(max_length=20)),
                ('owner', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='asik',
            old_name='lmp_eth_ip',
            new_name='lmp_ip',
        ),
        migrations.RemoveField(
            model_name='abil',
            name='pn_num',
        ),
        migrations.RemoveField(
            model_name='abil',
            name='serial_type',
        ),
        migrations.RemoveField(
            model_name='asik',
            name='pn_num',
        ),
        migrations.RemoveField(
            model_name='asik',
            name='serial_type',
        ),
        migrations.AddField(
            model_name='abil',
            name='pn',
            field=models.CharField(default='123456', max_length=100),
        ),
        migrations.AddField(
            model_name='abil',
            name='serial_num',
            field=models.CharField(default='123456', max_length=20),
        ),
        migrations.AddField(
            model_name='asik',
            name='pn',
            field=models.CharField(default='123456', max_length=20),
        ),
        migrations.AddField(
            model_name='asik',
            name='serial_num',
            field=models.CharField(default='123456', max_length=50),
        ),
        migrations.AddField(
            model_name='classicalbts',
            name='location',
            field=models.CharField(default='123456', max_length=50),
        ),
    ]