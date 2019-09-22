from django.urls import path, include
from . import views

urlpatterns = [
  path('<str:department>/', views.DepartmentView.as_view(), name='department-filter')
]
