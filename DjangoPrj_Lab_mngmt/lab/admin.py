# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Asik, Abil, ClassicalBTS

# Register your models here.
class AsikAdmin(admin.ModelAdmin):
    list_display = ("id", "eth_ip", "lmp_eth_ip", "slot", "serial_type", "pn_num", "owner")
    list_filter = ("serial_type",)
    search_fields = ("eth_ip", "lmp_eth_ip", "serial_type", "owner")
    ordering = ["serial_type", "owner"]

class AbilAdmin(admin.ModelAdmin):
    list_display = ("id", "slot", "serial_type", "pn_num", "owner")
    list_filter = ("serial_type",)
    search_fields = ("eth_ip", "lmp_eth_ip", "serial_type", "owner")
    ordering = ["serial_type", "owner"]

class ClassicalBTSAdmin(admin.ModelAdmin):
    list_display = ("id", "asik_id", "abil_id", "owner")
    search_fields = ("owner",)


admin.site.register(Asik, AsikAdmin)
admin.site.register(Abil, AbilAdmin)
admin.site.register(ClassicalBTS, ClassicalBTSAdmin)