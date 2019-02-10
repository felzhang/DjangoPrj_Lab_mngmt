# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Gps(models.Model):
    serial_num = models.CharField(max_length=20, default="123456")
    owner = models.CharField(max_length=50, default="admin")

    # __str__定义， 当定义完model后，一般要定义__str__了，一个非常重要到用法：如果某个model通过onetoone关联到这个model后，此model在另一个model中到显示就是__str__定义内容
    # The str method defines a human-readable representation of the model that is displayed in the Django admin site and in the Django shell.
    def __str__(self):                      # 一般返回str，在html中都可以显示。如果定义成__int__，可能在页面显示不出来。
        return str(self.id)                 # id为init型，可以转换为str


class Asik(models.Model):
    eth_ip = models.GenericIPAddressField(unique=True, default="10.0.0.0")
    lmp_ip = models.GenericIPAddressField(default="192.168.255.1")
    pn = models.CharField(max_length=20, default="123456")
    serial_num = models.CharField(unique=True, max_length=50, default="123456")
    slot = models.CharField(max_length=10, default="3")
    gps = models.OneToOneField(Gps, null=True, on_delete=models.CASCADE)
    owner = models.CharField(max_length=50, default="admin")

    def __str__(self):
        return str(self.id)


class Abil(models.Model):
    pn = models.CharField(max_length=100, default="123456")
    serial_num = models.CharField(max_length=20, default="123456")
    slot = models.CharField(max_length=10, default="3")
    owner = models.CharField(max_length=20, default="admin")

    def __str__(self):
        return str(self.id)


class ClassicalBTS(models.Model):
    asik_id = models.IntegerField(default=0)
    abil_id = models.IntegerField(default=0)
    location = models.CharField(max_length=50, default="123456")
    owner = models.CharField(max_length=20, default="admin")

    def __str__(self):
        return str(self.id)