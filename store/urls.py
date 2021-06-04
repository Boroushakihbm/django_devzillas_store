from django.urls import path
from .views import DepartmentList, DepartmentDetail, AddDepartment

urlpatterns = [
    path('department/', DepartmentList.as_view()),
    path('department/<int:pk>/', DepartmentDetail.as_view()),
    path('department/add/', AddDepartment.as_view()),

]
