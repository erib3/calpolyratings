from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.PostFormView.as_view(), name = 'make_post'),
]
