# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-11 09:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0015_auto_20190211_0838'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pn', models.CharField(default='A.203', max_length=20)),
                ('sn', models.CharField(max_length=50, unique=True)),
                ('owner', models.CharField(default='admin', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rru',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pn', models.CharField(default='AEQA', max_length=20)),
                ('sn', models.CharField(max_length=50, unique=True)),
                ('owner', models.CharField(default='admin', max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='abil',
            name='serial_num',
        ),
        migrations.RemoveField(
            model_name='asik',
            name='serial_num',
        ),
        migrations.RemoveField(
            model_name='gps',
            name='serial_num',
        ),
        migrations.AddField(
            model_name='abil',
            name='sn',
            field=models.CharField(default=1, max_length=50, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='asik',
            name='sn',
            field=models.CharField(default=1, max_length=50, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gps',
            name='pn',
            field=models.CharField(default='FYGB', max_length=20),
        ),
        migrations.AddField(
            model_name='gps',
            name='sn',
            field=models.CharField(default=1, max_length=50, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='abil',
            name='owner',
            field=models.CharField(default='admin', max_length=50),
        ),
        migrations.AlterField(
            model_name='abil',
            name='pn',
            field=models.CharField(default='A.102', max_length=20),
        ),
        migrations.AlterField(
            model_name='abil',
            name='slot',
            field=models.CharField(default='1', max_length=10),
        ),
        migrations.AlterField(
            model_name='asik',
            name='eth_ip',
            field=models.GenericIPAddressField(default='10.1.1.2', unique=True),
        ),
        migrations.AlterField(
            model_name='asik',
            name='gps',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lab.Gps'),
        ),
        migrations.AlterField(
            model_name='asik',
            name='pn',
            field=models.CharField(default='A.101', max_length=20),
        ),
        migrations.AlterField(
            model_name='asik',
            name='slot',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AlterField(
            model_name='classicalbts',
            name='abil_id',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lab.Abil'),
        ),
        migrations.AlterField(
            model_name='classicalbts',
            name='asik_id',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lab.Asik'),
        ),
        migrations.AlterField(
            model_name='classicalbts',
            name='location',
            field=models.CharField(default='GR_08_SLOT_0', max_length=50),
        ),
        migrations.AddField(
            model_name='abil',
            name='rru',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lab.Rru'),
        ),
        migrations.AddField(
            model_name='classicalbts',
            name='amia_id',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lab.Amia'),
        ),
    ]