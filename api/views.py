""" from django.shortcuts import render
from django.http import JsonResponse """
from students.models import Student
from .serializers import StudentSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def student_data(request):
    if request.method == 'GET':
        student = Student.objects.all()
        serializer = StudentSerializers(student, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)