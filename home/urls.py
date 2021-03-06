from django.urls import path, include
from . import views
from teacher_profile.views import AddTeacher
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('add-teacher/', AddTeacher.as_view(), name='add_professor'),
    path('core/', include('core.urls')),
    path('department/', include('department_courses.urls')),
    path('<slug:teacher_name>/', include('teacher_profile.urls'))
]
