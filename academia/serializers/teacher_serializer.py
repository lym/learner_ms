from rest_framework.serializers import ModelSerializer
from academia.models import Teacher


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'name'] # TODO: Add 'students'
