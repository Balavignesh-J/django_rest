from django.urls import path
from . import views

urlpatterns = [
    path("student/", view=views.student_data, name='student_data'),
    path("student/<int:pk>", view=views.studentdetailview, name='one_student')
]
