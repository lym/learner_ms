from django.shortcuts import get_object_or_404, render
from django.template import loader

from django.http import HttpResponse

from academia.models import Student, Teacher

def index(request):
    template = loader.get_template("academia/home.html")
    context = {}
    return HttpResponse(template.render(context, request))

def students_index(request):
    students = Student.objects.all()
    template = loader.get_template("academia/students_index.html")
    context = {"students": students}
    return HttpResponse(template.render(context, request))

def student_show(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    teachers = student.teacher_set.all()
    template = loader.get_template("academia/student_show.html")
    context = {"student": student, "teachers": teachers}
    return HttpResponse(template.render(context, request))

def student_edit(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    template = loader.get_template("academia/student_edit.html")
    context = {"student": student}
    return HttpResponse(template.render(context, request))

def teachers_index(request):
    teachers = Teacher.objects.all()
    template = loader.get_template("academia/teachers_index.html")
    context = {"teachers": teachers}
    return HttpResponse(template.render(context, request))

def teacher_show(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    students = teacher.students.all()
    template = loader.get_template("academia/teacher_show.html")
    context = {"students": students, "teacher": teacher}
    return HttpResponse(template.render(context, request))

def teacher_edit(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    template = loader.get_template("academia/teacher_edit.html")
    context = {"teacher": teacher}
    return HttpResponse(template.render(context, request))
