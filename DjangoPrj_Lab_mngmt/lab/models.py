# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Amia(models.Model):
    pn = models.CharField(max_length=20, default="A.203")
    sn = models.CharField(unique=True, max_length=50)
    owner = models.CharField(max_length=50, default="admin")

    def __str__(self):
        return str(self.id)

class Gps(models.Model):
    pn = models.CharField(max_length=21, default="FYGB")
    sn = models.CharField(unique=True, max_length=50)
    owner = models.CharField(max_length=50, default="admin")

    def __str__(self):
        return str(self.id)

class Pb(models.Model):
    ip = models.GenericIPAddressField(unique=True, default="10.1.1.3")
    sn = models.CharField(max_length=50, unique=True)
    owner = models.CharField(max_length=50, default="admin")

    def __str__(self):
        return str(self.id)

class Rru(models.Model):
    pn = models.CharField(max_length=20, default="AEQA")
    sn = models.CharField(unique=True, max_length=50)
    owner = models.CharField(max_length=50, default="admin")

    def __str__(self):
        return str(self.id)

class Asik(models.Model):
    eth_ip = models.GenericIPAddressField(unique=True, default="10.1.1.2")
    lmp_ip = models.GenericIPAddressField(default="192.168.255.1")
    pn = models.CharField(max_length=20, default="A.101")
    sn = models.CharField(unique=True, max_length=50)
    slot = models.CharField(max_length=10, default="0")
    # on_delete默认为CASCADE，级联删除：Gps删除后，包含此Gps到Asik自动删除。
    #               SET_NULL 删除关联数据,与之关联的值设置为null, 即Gps删除后，包含此Gps到Asik将此项设置为null， 前提是null=True, blank=True
    #               SET_DEFAULT 删除关联数据,与之关联的值设置为默认值, 前提是设置了default值 default=1
    gps = models.OneToOneField(Gps, null=True, blank=True, on_delete=models.SET_NULL)
    owner = models.CharField(max_length=50, default="admin")
    # __str__定义， 当定义完model后，一般要定义__str__了，一个非常重要到用法：如果某个model通过onetoone关联到这个model后，此model在另一个model中到显示就是__str__定义内容
    # The str method defines a human-readable representation of the model that is displayed in the Django admin site and in the Django shell.
    def __str__(self):                      # 一般返回str，在html中都可以显示。如果定义成__int__，可能在页面显示不出来。
        return str(self.id)                 # id为init型，可以转换为str

class Abil(models.Model):
    pn = models.CharField(max_length=20, default="A.102")
    sn = models.CharField(unique=True, max_length=50)
    slot = models.CharField(max_length=10, default="1")
    rru = models.OneToOneField(Rru, null=True, blank=True, on_delete=models.SET_NULL)
    owner = models.CharField(max_length=50, default="admin")

    def __str__(self):
        return str(self.id)

class ClassicalBTS(models.Model):
    PB_PORT_CHOICES=(
        ('1', 'PORT_1'),
        ('2', 'PORT_2'),
        ('3', 'PORT_3'),
        ('4', 'PORT_4'),
        ('5', 'PORT_5'),
        ('6', 'PORT_6'),
        ('7', 'PORT_7'),
        ('8', 'PORT_8'),
        )
    amia_id = models.OneToOneField(Amia, null=True, blank=True, on_delete=models.SET_NULL)
    asik_id = models.OneToOneField(Asik, null=True, blank=True, on_delete=models.SET_NULL)
    abil_id = models.OneToOneField(Abil, null=True, blank=True, on_delete=models.SET_NULL)
    location = models.CharField(max_length=50, default="GR_08_SLOT_0")
    pb_id = models.OneToOneField(Pb, null=True, blank=True, on_delete=models.SET_NULL)
    pb_port = models.CharField(choices=PB_PORT_CHOICES, max_length=20, null=True, blank=True)
    tag = models.CharField(max_length=50, null=True, blank=True)
    owner = models.CharField(max_length=20, default="admin")

    def __str__(self):
        return str(self.id)