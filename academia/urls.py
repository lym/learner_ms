from django.urls import path, include
from rest_framework.routers import DefaultRouter
from academia.views import (
    StudentViewSet,
    TeacherViewSet,
    students_index,
    student_show,
    teachers_index,
    teacher_show,
)

from . import views

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'teachers', TeacherViewSet)

urlpatterns = [
    # path("", views.index, name="index"),
    path("students", students_index, name='students-index'),
    path("students/<int:student_id>/", student_show, name='student-show'),
    path("teachers", teachers_index, name='teachers-index'),
    path("teachers/<int:teacher_id>/", teacher_show, name='teacher-show'),
]
