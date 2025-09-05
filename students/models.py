from django.db import models

# Create your models here.

class Student(models.Model):
    student_name = models.CharField(max_length=50)
    student_dept = models.CharField(max_length=50)
    student_age = models.IntegerField()

    def __str__(self):
        return self.student_name