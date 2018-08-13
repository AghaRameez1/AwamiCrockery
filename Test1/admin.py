# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from Test1.models import vendorModel

# Register your models here.


class vendorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'price', 'item_code']

admin.site.register(vendorModel, vendorAdmin)