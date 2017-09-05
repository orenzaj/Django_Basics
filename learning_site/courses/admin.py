# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# First import your models
from .models import Course
from .models import Step


# These classes will enable editing multiple steps within the course.
class StepInline(admin.StackedInline):
    model = Step

class CourseAdmin(admin.ModelAdmin):
    inlines = [StepInline,]

# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(Step)
