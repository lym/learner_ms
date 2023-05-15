from django.urls import path, include
from rest_framework.routers import DefaultRouter
from academia.views import StudentViewSet, TeacherViewSet

from . import views

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'teachers', TeacherViewSet)

urlpatterns = [
    # path("", views.index, name="index"),
]
