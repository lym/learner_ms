from django.shortcuts import render
from django.template import loader

from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome, student!")

def students_index(request):
    template = loader.get_template("academia/students_index.html")
    context = {}
    return HttpResponse(template.render(context, request))

def student_show(request, student_id):
    return HttpResponse("Welcome to student with ID %s" % student_id)

def teachers_index(request):
    template = loader.get_template("academia/teachers_index.html")
    context = {}
    return HttpResponse(template.render(context, request))

def teacher_show(request, teacher_id):
    return HttpResponse("Welcome to teacher with ID %s" % teacher_id)
