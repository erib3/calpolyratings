from django.db import models
from django.db.models.signals import post_save, post_delete, pre_save
from django.core.mail import send_mail
from django.dispatch import receiver
from django.conf import settings

from model_utils import FieldTracker
from core.models import TimeStampModel
from teacher_profile.models import Teacher_profile
from department_courses.models import Course, Department
from cpratings.use_secrets import *

# This is the outline for a Post data model object. 
class Post(TimeStampModel):
    QUARTERS = ( ('Fall', ("Fall")),
    ('Winter', ("Winter")),
    ('Spring', ("Spring")),
    ('Summer', ("Summer"))
    )

    OVERALL = (
    ("A+", ("A+")),
    ("A", ("A")),
    ("A-", ("A-")),
    ("B+", ("B+")),
    ("B", ("B")),
    ('B-', ("B-")),
    ("C+", ("C+")),
    ("C", ("C")),
    ("C-", ("C-")),
    ('D', ("D")),
    ("F", ("F"))
    )
    
    DIFFICULTY = (
    (1, ("1")), #- very easy course
    (2, ("2")),
    (3, ("3")),
    (4, ("4")),
    (5, ("5")), #- requires work, but doablef
    (6, ("6")),
    (7, ("7")),
    (8, ("8")),
    (9, ("9")),
    (10, ("10")) # - extremely difficult
    )
    teacher = models.ForeignKey(Teacher_profile, on_delete=models.PROTECT)
    
    overall_rating_num = models.IntegerField(default=0)
    difficulty_rating = models.IntegerField(choices=DIFFICULTY, null=True)
    grade_received = models.CharField(max_length=2, choices=OVERALL, null=True)

    course_abbrv = models.CharField(max_length=5)
    course_num = models.IntegerField()

    course = models.ForeignKey(Course, on_delete=models.PROTECT)

    compact_text = models.TextField(null=True, blank=True)
    post = models.TextField()

    polyratings_post = models.BooleanField(default=False)

    quarter_taken = models.CharField(max_length=6, choices=QUARTERS, null=True)
    year_taken = models.IntegerField(null=True)

    tracker = FieldTracker()

    def save(self, *args, **kwargs):

        department = Department.objects.get(abbreviation=self.course_abbrv)
        course, created = Course.objects.get_or_create(department=department, course_num=self.course_num)
        self.course = course
        self.teacher.courses.add(course)

        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.teacher) + " " + str(self.id)

@receiver(post_save, sender=Post)
def send_email(sender, **kwargs):
    if settings.DEBUG:
        return
    post = "compact post \n\n" + kwargs['instance'].compact_text.__str__() + "\n\n full post \n\n" + kwargs['instance'].post.__str__()
    # TODO: make this msg better
    msg = 'A new post was submitted for ' + kwargs['instance'].teacher.__str__() + " " + 'it reads \n\n' + post
    send_mail('A new post!', msg, get_secret("OUT_EMAIL"), [get_secret("ADMIN_EMAIL")], fail_silently=False)


@receiver(post_save, sender=Post)
def update_fields_save(sender, **kwargs):
	
	the_post = kwargs['instance']
	teacher = the_post.teacher
	posts = Post.objects.filter(teacher=teacher)
	created = kwargs.get('created', False) 

	# total posts - polyratings_posts
	num_cpratings_posts = posts.count() - posts.filter(polyratings_post=True).count()

	previous_teacher = the_post.tracker.previous('teacher_id') 

	if posts.count() > teacher.evaluations:  # post added
                total_overall_rating = ((num_cpratings_posts-1) * teacher.overall_rating) + the_post.overall_rating_num
                total_overall_difficulty = ((num_cpratings_posts-1) * teacher.overall_difficulty) + the_post.difficulty_rating
                teacher.evaluations = posts.count() 
                set_teacher_rating(teacher,total_overall_rating, total_overall_difficulty, num_cpratings_posts)
	else: 			 # update
		prev_course_id = the_post.tracker.previous('course_id')

		# course change
		if prev_course_id != the_post.course.id:
                    prev_course = Course.objects.get(id=prev_course_id)
                    update_courses(prev_course, posts, teacher)	

		prev_overall = the_post.tracker.previous('overall_rating_num')
		prev_difficulty = the_post.tracker.previous('difficulty_rating')

		# grading change 
		if(prev_overall != the_post.overall_rating_num or prev_difficulty != the_post.difficulty_rating):
                        total_overall_rating = (num_cpratings_posts * teacher.overall_rating) - prev_overall + the_post.overall_rating_num
                        total_overall_difficulty = (num_cpratings_posts * teacher.overall_difficulty) - prev_difficulty + the_post.difficulty_rating

                        set_teacher_rating(teacher,total_overall_rating, total_overall_difficulty, num_cpratings_posts)
	teacher.save()

@receiver(post_delete, sender=Post)
def update_fields_delete(sender, **kwargs):
  the_post = kwargs['instance']
  teacher = the_post.teacher
  posts = Post.objects.filter(teacher=teacher)
  created = kwargs.get('created', False) 

  # total posts - polyratings_posts
  num_cpratings_posts = posts.count() - posts.filter(polyratings_post=True).count()

  previous_teacher = the_post.tracker.previous('teacher_id') 

  # we delete a polyratings post
  if the_post.polyratings_post:     
    if posts.count() < teacher.evaluations: #delete
      update_courses(the_post.course, posts, teacher)
      teacher.evaluations = posts.count()

  # normal calpolyratings post deleted
  elif posts.count() < teacher.evaluations:
    update_courses(the_post.course, posts, teacher)

    total_overall_rating = ((num_cpratings_posts + 1) * teacher.overall_rating) - the_post.overall_rating_num
    total_overall_difficulty = ((num_cpratings_posts + 1) * teacher.overall_difficulty) - the_post.difficulty_rating

    teacher.evaluations = posts.count()
    set_teacher_rating(teacher,total_overall_rating, total_overall_difficulty, num_cpratings_posts)

  teacher.save()

def update_courses(course, posts, teacher):
    if course == None:
        return
    if posts.filter(course=course).count() == 0:
        teacher.courses.remove(course) 

def set_teacher_rating(teacher, total_overall_rating, total_overall_difficulty, num_cpratings_posts):
    if(num_cpratings_posts != 0):
        teacher.overall_rating = total_overall_rating / num_cpratings_posts
        teacher.overall_difficulty = total_overall_difficulty / num_cpratings_posts
    else:
        teacher.overall_rating = -1
        teacher.overall_difficulty = -1
