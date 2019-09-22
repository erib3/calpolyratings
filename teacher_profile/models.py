from django.db import models
from django.template.defaultfilters import slugify
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator

from department_courses.models import Department, Course
from cpratings.use_secrets import *

class Teacher_profile(models.Model):
    alphanumeric = RegexValidator(r'^[a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    first_name = models.CharField(max_length=30, validators=[alphanumeric])
    last_name = models.CharField(max_length=30, validators=[alphanumeric])
    full_name = models.CharField(max_length=60, blank=True)

    overall_rating = models.DecimalField(max_digits=4, decimal_places=2, default=-1)
    overall_difficulty = models.DecimalField(max_digits=4, decimal_places=2, default=-1)

    evaluations = models.IntegerField(default=0)

    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True)

    courses = models.ManyToManyField(Course)

    def save(self, *args, **kwargs):
        self.first_name = self.first_name.capitalize()
        self.last_name = self.last_name.capitalize()


        self.full_name = self.first_name + " " + self.last_name
        self.slug = slugify(self.first_name + ' ' + self.last_name)
        super(Teacher_profile, self).save(*args, **kwargs)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

@receiver(post_save, sender=Teacher_profile)
def send_email(sender, **kwargs):
  print(kwargs)
  if kwargs['instance'].evaluations == 0:
    msg = 'Hi there, a new teacher was added to the site \n' + kwargs['instance'].__str__() + ' -- ' + kwargs['instance'].department.__str__()
    send_mail('A new teacher !', msg, 'cpratings', [get_secret("EMAIL")], fail_silently=False)
