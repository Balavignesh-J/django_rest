from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("employee", viewset=views.Employee_viewset, basename='employees')
urlpatterns = [
    path("student/", view=views.student_data, name='student_data'),
    path("student/<int:pk>", view=views.studentdetailview, name='one_student'),
    #path("employee/", view=views.Employee_view.as_view(), name='employees'),
    #path("employee/<int:pk>", view=views.Employee_single.as_view(), name='one_employ'),
    path("",include(router.urls)),
    path("blog/", views.Blog_view.as_view(), name="Blog"),
    path("comment/", views.Comment_view.as_view(), name="Comment"),
    path("blog/<int:pk>/", views.BlogDetail_view.as_view(), name="Blogdetail"),
    path("comment/<int:pk>/", views.CommentDetail_view.as_view(), name="Commentdetail")
]
