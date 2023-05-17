from django.urls import path, include
from rest_framework.routers import DefaultRouter
from academia.views import (
    StudentViewSet,
    TeacherViewSet,
    index,
    students_index,
    student_show,
    student_edit,
    teachers_index,
    teacher_show,
    teacher_edit,
)

from . import views

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'teachers', TeacherViewSet)

urlpatterns = [
    path("", views.index, name="index"),
    path("students", students_index, name='students-index'),
    path("students/<int:student_id>/", student_show, name='student-show'),
    path("students/<int:student_id>/edit", student_edit, name='student-edit'),
    path("teachers", teachers_index, name='teachers-index'),
    path("teachers/<int:teacher_id>/", teacher_show, name='teacher-show'),
    path("teachers/<int:teacher_id>/edit", teacher_edit, name='teacher-edit'),
]
