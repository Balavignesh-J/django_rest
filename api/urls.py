from django.urls import path
from . import views

urlpatterns = [
    path("student/", view=views.student_data, name='student_data'),
    path("student/<int:pk>", view=views.studentdetailview, name='one_student'),
    path("employee/", view=views.Employee_view.as_view(), name='employees'),
    path("employee/<int:pk>", view=views.Employee_single.as_view(), name='one_employ'),
]
