from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic.edit import FormView
from django import forms
from django.urls import reverse

from teacher_profile.models import Teacher_profile
from department_courses.models import Course, Department 
from .forms import PostForm 
from utilities import recaptcha_check 

#View handles 'Posts'. It responds to get and post requests from using trying to make a post on a teacher
class PostFormView(FormView):
    template_name = 'postings/post_form.html'
    form_class = PostForm

    #method returns the url string to get back to the teacher profile page after submitting
    def get_success_url(self, request, teacher_name):
        return ('/%s/' % teacher_name)

    def get(self, request, teacher_name, *args, **kwargs):
      form = self.form_class(initial=self.initial)
      teacher = Teacher_profile.objects.get(slug=teacher_name)
      departments = Department.objects.all()
      return render(request, self.template_name, {'departments': departments, 'form': form, 'slug':teacher_name, 'teacher':teacher })

    def post(self, request, teacher_name, *args, **kwargs):
      form = PostForm(request.POST)
    
      print(request.POST)
      if form.is_valid():

        recaptcha_response = request.POST.get('captcha')
        recaptcha_valid = recaptcha_check(recaptcha_response)

        if recaptcha_valid:
          obj = form.save(commit=False)
          obj.teacher= Teacher_profile.objects.get(slug=teacher_name)
          obj.save()
          return HttpResponseRedirect(self.get_success_url(request, teacher_name))

      return HttpResponse('<h1>something is not right</h1>')

    
