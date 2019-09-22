from django.forms import ModelForm
from .models import Post #change model location

class PostForm(ModelForm):
  class Meta:
    model = Post
    fields = ['overall_rating_num', 
              'difficulty_rating', 
              'grade_received', 
              'quarter_taken', 
              'year_taken', 
              'post', 
              'compact_text', 
              'course_num',
              'course_abbrv']

