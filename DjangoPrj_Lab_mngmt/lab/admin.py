# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Asik, Abil, ClassicalBTS, Gps

# Register your models here.
class AsikAdmin(admin.ModelAdmin):
    list_display = ("id", "eth_ip", "lmp_ip", "pn", "sn", "slot", "gps_id", "owner")
    list_filter = ("sn",)
    search_fields = ("eth_ip", "lmp_ip", "sn", "owner")
    ordering = ["sn", "owner"]

class AbilAdmin(admin.ModelAdmin):
    list_display = ("id", "slot", "pn", "sn", "owner")
    list_filter = ("sn",)
    search_fields = ("sn", "owner")
    ordering = ["sn", "owner"]

class ClassicalBTSAdmin(admin.ModelAdmin):
    list_display = ("id", "asik_id", "abil_id", "location", "owner")
    search_fields = ("owner",)

class GpsAdmin(admin.ModelAdmin):
    list_display = ("id", "sn", "owner")
    list_filter = ("sn", "owner")
    search_fields = ("owner",)
    ordering = ["id"]

admin.site.register(Asik, AsikAdmin)
admin.site.register(Abil, AbilAdmin)
admin.site.register(ClassicalBTS, ClassicalBTSAdmin)
admin.site.register(Gps, GpsAdmin)