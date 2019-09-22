from django.urls import path, include
from . import views
from teacher_profile.views import AddTeacher
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('faq/', views.Faq.as_view(), name='faq'),
    path('add-teacher/', AddTeacher.as_view(), name='add_professor'),
    path('core/', include('core.urls')),
    path('department/', include('department_courses.urls')),
    path('<slug:teacher_name>/', include('teacher_profile.urls'))
]
