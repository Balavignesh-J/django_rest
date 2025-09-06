#from django.shortcuts import render
from django.http import Http404
from students.models import Student
from .serializers import StudentSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from employees.models import Employees
from .serializers import EmployeeSerializers

from rest_framework import generics,mixins

@api_view(['GET','POST'])
def student_data(request):
    if request.method == 'GET':
        student = Student.objects.all()
        serializer = StudentSerializers(student, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def studentdetailview(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = StudentSerializers(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = StudentSerializers(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
""" class Employee_view(APIView):
    def get(self, request):
        employee = Employees.objects.all()
        serializer = EmployeeSerializers(employee, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = EmployeeSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) """
    
""" class Employee_single(APIView):
    def get_obj(self, pk):
        try:
            employee =  Employees.objects.get(pk=pk)
        except Employees.DoesNotExist:
            raise Http404
        return employee
        
    def get(self, request, pk):
        employee = self.get_obj(pk)
        serializer = EmployeeSerializers(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        employee = self.get_obj(pk)
        serializer = EmployeeSerializers(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        employee = self.get_obj(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) """
    
class Employee_view(mixins.CreateModelMixin,mixins.ListModelMixin,generics.GenericAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializers

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
class Employee_single(mixins.RetrieveModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin,generics.GenericAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializers

    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)