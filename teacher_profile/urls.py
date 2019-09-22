from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.teacher_profile, name='dd'),
    path('post/', include('postings.urls')),
    path('compacttextmode/', views.CompactTextMode),
    path('fullpostmode/', views.FullPostMode),
    path('<slug:course_filter>/', views.ClassFilter)
]
