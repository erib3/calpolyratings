from django.shortcuts import render
from django.views.generic.list import ListView

from teacher_profile.models import Teacher_profile
from .models import Department

class DepartmentView(ListView):
  model = Teacher_profile
  template_name = 'home/home.html'  

  ordering = 'full_name'
  context_object_name = 'teacher_profiles'   # your own name for the list as a template variable

  paginate_by = 20

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['selection'] = Department.objects.get(slug=self.kwargs['department'])
      context['departments'] = Department.objects.all()
      print(context)
      return context

  def get_queryset(self): 
    department_obj = Department.objects.get(slug=self.kwargs['department'])
    queryset = Teacher_profile.objects.filter(department=department_obj).order_by('full_name')

    return queryset
