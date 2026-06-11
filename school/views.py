from django.shortcuts import render

from django.views.generic import ListView

from .models import Student


def students_list(request):
    template = "school/students_list.html"
    ordering = "group"
    students = Student.objects.all().order_by(ordering).prefetch_related("teachers")
    context = {"object_list": students}

    return render(request, template, context)
