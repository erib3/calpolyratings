from django.db import models
from django.template.defaultfilters import slugify

class Department(models.Model):
    name = models.CharField(max_length=50, unique=True)
    abbreviation = models.CharField(max_length=5, unique=True)
    slug = models.SlugField(unique=True, blank=True)
	
    def save(self, *args, **kwargs):
      self.slug = slugify(self.name)
      super(Department, self).save(*args, **kwargs)

    def __str__(self):
      if(len(self.name) > 32):
        return self.abbreviation
      return self.name
      

class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course_num = models.IntegerField()
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.department.abbreviation + " " + str(self.course_num))
        super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return self.department.abbreviation + ' ' + str(self.course_num)
