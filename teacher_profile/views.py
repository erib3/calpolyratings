from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.views import View
from django.views.generic.edit import FormView
from django.views.generic.list import ListView


from department_courses.models import Course
from postings.models import Post
from utilities import recaptcha_check
from .forms import TeacherForm
from .models import Teacher_profile

# View returns teacher profile page given a slug
# Returns up to 10 posts
def teacher_profile(request, teacher_name):
    out_of_posts = False
    profile = get_object_or_404(Teacher_profile, slug=teacher_name)
    posts = Post.objects.filter(teacher=profile)
    post_subset = posts.order_by('-created').order_by('polyratings_post')[:10]


    courses = profile.courses.all().order_by('slug')
    if posts.count() <= 10 :
      out_of_posts = True
    return render(request, 'teacher_profile/teacher_profile.html', {'profile': profile, 'out_of_posts': out_of_posts,'posts':post_subset, 'courses':courses})


# View handles adding new teachers to site
class AddTeacher(FormView):
  template_name = 'teacher_profile/teacher_form.html'
  form_class = TeacherForm


  # Returns the form
  def get(self, request, *args, **kwargs):
    form = self.form_class(initial=self.initial)
    return render(request, self.template_name, {'form': form})

  # Validates the form and adds to db
  # Redirects to teacher's new page
  def post(self, request, *args, **kwargs):
    form = TeacherForm(request.POST)
    if form.is_valid():

      fullname = form.cleaned_data['first_name'] + " " + form.cleaned_data['last_name']

      # check if full name is already in our database 
      if(Teacher_profile.objects.filter(full_name=fullname).exists()):
        return HttpResponseRedirect('/' + Teacher_profile.objects.get(full_name=fullname).slug) 

      recaptcha_response = request.POST.get('captcha')
      recaptcha_valid = recaptcha_check(recaptcha_response)

      if recaptcha_valid:
        new_profile = form.save()
        url = '/' + new_profile.slug
        return HttpResponseRedirect(url)

    return HttpResponse('<h1>something is not right</h1>')

def ClassFilter(request, teacher_name, course_filter):

  out_of_posts = False
  # start is used to represent the range of posts we need to return
  if request.GET.get('start'):
    start = int(request.GET.get('start'))
  else:
    start=0
	

  teacher = Teacher_profile.objects.get(slug=teacher_name)
  course = Course.objects.get(slug=course_filter)
  queryset = Post.objects.filter(teacher=teacher, course=course).order_by('-created').order_by('polyratings_post')

  size_posts = queryset.count()

  if start+10 >= size_posts:
    queryset = queryset[start:size_posts]
    out_of_posts = True
  else: 
    queryset = queryset[start : start+10]
  

  return render(request, 'teacher_profile/full_posts.html', {'posts': queryset, 'out_of_posts':out_of_posts})



# View that is invoked for AJAX in FullPostMode
# returns the next 10 posts to display or ''
def FullPostMode(request, teacher_name):

  out_of_posts = False

  # start is used to represent the range of posts we need to return

  if request.GET.get('start'):
    start = int(request.GET.get('start'))
  else:
    start=0
	
  ##print('start: ' + str(start))

  teacher = Teacher_profile.objects.get(slug=teacher_name)
  queryset = Post.objects.filter(teacher=teacher).order_by('-created').order_by('polyratings_post')

  size_posts = queryset.count()
	
  if start+10 >= size_posts:
    queryset = queryset[start:size_posts]
    out_of_posts = True
  else: 
    queryset = queryset[start : start+10]
    #print(queryset)
  return render(request, 'teacher_profile/full_posts.html', {'posts': queryset, 'out_of_posts': out_of_posts})

# View that is invoked when AJAX kicks in for NiceTextMode
# should return next 10 posts or ''
def CompactTextMode(request, teacher_name):
  out_of_posts = False

  if request.GET.get('start'):
    start = int(request.GET.get('start'))
  else:
    start=0

  #print('start: ' + str(start))
  teacher = Teacher_profile.objects.get(slug=teacher_name)
  #limit queryset to the range, determined by start

  queryset = Post.objects.filter(teacher=teacher, polyratings_post=False).order_by('-created')

  size_posts = queryset.count()
  print("size of posts: " + str(queryset.count()))
  if start+10 >= size_posts:
    queryset = queryset[start:size_posts]
    out_of_posts = True
  else: 
    queryset = queryset[start : start+10]
  return render(request, 'teacher_profile/compact_posts.html', {'posts': queryset, 'out_of_posts': out_of_posts})


