from django.forms import ModelForm
from teacher_profile.models import Teacher_profile

class TeacherForm(ModelForm):
  class Meta:
    model = Teacher_profile
    fields = ['first_name', 'last_name', 'department']