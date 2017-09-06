# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
# render takes 3 args:
#   request (same parameter as view)
#   template_path
#   context (dictionary)

from .models import Course, Step
# Create your views here.
# This will display a list of all the courses.


def course_list(request):
    courses = Course.objects.all()      # query all courses in Course model
    return render(request, 'courses/course_list.html', {'courses': courses})


def course_detail(request, pk):
    #course = Course.objects.get(pk=pk)
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})


def step_detail(request, course_pk, step_pk):
    step = get_object_or_404(Step, course_id=course_pk, pk=step_pk)
    return render(request, 'courses/step_detail.html', {'step': step})
