from rest_framework.serializers import ModelSerializer
from academia.models import Student

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'surname',] # TODO: Add 'teachers'
