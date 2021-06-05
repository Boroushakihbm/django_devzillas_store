from django.urls import path
from .views.department import DepartmentList, DepartmentDetail, AddDepartment
from .views.feature import AddFeature, FeatureDetail, FeatureList

urlpatterns = [
    path('department/', DepartmentList.as_view()),
    path('department/<int:pk>/', DepartmentDetail.as_view()),
    path('department/add/', AddDepartment.as_view()),
    path('feature/', FeatureList.as_view()),
    path('feature/<int:pk>/', FeatureDetail.as_view()),
    path('feature/add/', AddFeature.as_view()),

]
