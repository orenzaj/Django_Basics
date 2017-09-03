# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render     # 3 args:
                                        #   request (same parameter as view)
                                        #   template_path
                                        #   context (dictionary)

from .models import Course
# Create your views here.
# This will display a list of all the courses.
def course_list(request):
    courses = Course.objects.all()      # query all courses in Course model
    return render(request, 'courses/course_list.html', {'courses': courses})
