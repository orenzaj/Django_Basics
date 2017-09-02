# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models        # Need this import for models

# Models are conventionally singular and will always inherit from models.Model
class Course(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
