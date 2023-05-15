from rest_framework.viewsets import ModelViewSet
from academia.models import Student
from academia.serializers import StudentSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
