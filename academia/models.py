from django.db import models


class Student(models.Model):
    name    = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name     = models.CharField(max_length=50)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name
