# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class vendorModel(models.Model):
    first_name = models.TextField(max_length=255)
    last_name = models.TextField(max_length=255)
    price = models.IntegerField(default=0)
    item_code = models.CharField(max_length=255,null=True, blank=True)