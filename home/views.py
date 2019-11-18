from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from teacher_profile.models import Teacher_profile
from postings.models import Post
from department_courses.models import Department


# View handles the home page, i.e. search bar, filters, and teacher profiles in groups of 20
class HomeView(ListView):
  model = Teacher_profile
  object_list = Teacher_profile.objects.all().order_by('full_name') 
  context_object_name='teacher_profiles'
  queryset = Teacher_profile.objects.all()
  paginate_by = 20


  def get(self, request, *args, **kwargs):
    self.kwargs['template'] = 'home/home'
    context = self.get_context_data(**kwargs)
    teacher_profiles = Teacher_profile.objects.all()
    context['departments'] = Department.objects.all()
	
    query = request.GET.get('q')

    if query:
      teacher_profiles = teacher_profiles.filter(full_name__icontains=query)
      context['teacher_profiles'] = teacher_profiles[:20]
      context['is_paginated'] = False

      if teacher_profiles.count() == 0:
        # set the context so we can still display the 'failed_search_query' in the search bar
        context['failed_search_query'] = query
        self.kwargs['template'] = 'home/no_search_results'

    return self.render_to_response(context)
    
  # overwritten method that returns template name from self.kwargs
  def get_template_names(self):
    return ['%s.html' % self.kwargs['template']]


  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['top'] = True
      return context




