# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Asik(models.Model):
    eth_ip = models.GenericIPAddressField()
    lmp_eth_ip = models.GenericIPAddressField(default="192.168.255.1")
    serial_type = models.CharField(max_length=20)
    pn_num = models.CharField(max_length=100)
    slot = models.CharField(max_length=10, default="3")
    gps_id = models.IntegerField(default=0)
    owner = models.CharField(max_length=50)

    def __str__(self):
        return self.pn_num


class Abil(models.Model):
    serial_type = models.CharField(max_length=20)
    pn_num = models.CharField(max_length=100)
    slot = models.CharField(max_length=10, default="3")
    owner = models.CharField(max_length=20, default="admin")

    def __str__(self):
        return self.pn_num


class ClassicalBTS(models.Model):
    asik_id = models.IntegerField(default=0)
    abil_id = models.IntegerField(default=0)
    owner = models.CharField(max_length=20, default="admin")