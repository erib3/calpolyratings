from django.urls import path, include
from . import views

urlpatterns = [
    path('footer/', views.footer, name='footer')
]
