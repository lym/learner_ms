from rest_framework.viewsets import ModelViewSet
from academia.models import Teacher
from academia.serializers import TeacherSerializer


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
