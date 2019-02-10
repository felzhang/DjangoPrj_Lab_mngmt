# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Asik, Abil, ClassicalBTS, Gps

# Register your models here.
class AsikAdmin(admin.ModelAdmin):
    list_display = ("id", "eth_ip", "lmp_ip", "pn", "serial_num", "slot", "gps_id", "owner")
    list_filter = ("serial_num",)
    search_fields = ("eth_ip", "lmp_ip", "serial_num", "owner")
    ordering = ["serial_num", "owner"]

class AbilAdmin(admin.ModelAdmin):
    list_display = ("id", "slot", "pn", "serial_num", "owner")
    list_filter = ("serial_num",)
    search_fields = ("eth_ip", "lmp_ip", "serial_num", "owner")
    ordering = ["serial_num", "owner"]

class ClassicalBTSAdmin(admin.ModelAdmin):
    list_display = ("id", "asik_id", "abil_id", "location", "owner")
    search_fields = ("owner",)

class GpsAdmin(admin.ModelAdmin):
    list_display = ("id", "serial_num", "owner")
    list_filter = ("serial_num", "owner")
    search_fields = ("owner",)
    ordering = ["id"]

admin.site.register(Asik, AsikAdmin)
admin.site.register(Abil, AbilAdmin)
admin.site.register(ClassicalBTS, ClassicalBTSAdmin)
admin.site.register(Gps, GpsAdmin)