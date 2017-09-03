# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

from .models import Course
# Create your views here.
# This will display a list of all the courses.
def course_list(request):
    courses = Course.objects.all()      # query all courses in Course model
    output = ',\n'.join(str(course) for course in courses)   # make a string with given queryset
    return HttpResponse(output)
