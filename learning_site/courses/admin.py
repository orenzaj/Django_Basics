# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# First import your model
from .models import Course

# Register your models here.
admin.site.register(Course)
admin.site.register(Step)
