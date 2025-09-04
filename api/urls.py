from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.student_data, name='student_data')
]
