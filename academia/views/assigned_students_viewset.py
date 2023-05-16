from django.http import Http404
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.views import APIView
from academia.models import Student, Teacher
from academia.serializers import StudentSerializer


class AssignedStudentsViewSet(APIView):
    def get(self, request, pk=None):
        teacher = self.get_teacher(pk)
        students = teacher.students
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request, pk=None):
        teacher = self.get_teacher(pk)
        students_data = request.data

        new_students_instance_ids = []
        for student in students_data:
            Student.objects.create(**student)
            most_recent = Student.objects.last()
            new_students_instance_ids.append(most_recent.id)
        teacher_students = Student.objects.filter(
            id__in=new_students_instance_ids
        )

        if teacher.students is None:
            teacher.students.set(*teacher_students)
        else:
            teacher.students.add(*teacher_students)

        serializer = StudentSerializer(teacher_students, many=True)
        return Response(serializer.data, status=HTTP_201_CREATED)

    def get_teacher(self, teacher_pk):
        try:
            return Teacher.objects.get(pk=teacher_pk)
        except Teacher.DoesNotExist:
            raise Http404('Teacher record not found')
