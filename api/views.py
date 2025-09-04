from django.shortcuts import render
from django.http import JsonResponse

def student_data(request):
    data = {'id':1, 'name':"harish", "age":21}
    return JsonResponse(data=data)