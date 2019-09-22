from django.test import TestCase

from .models import Teacher_profile
from core import populate_departments

from department_courses.models import Department, Course
from postings.models import Post

class TeacherprofileViewTesting(TestCase):

  @classmethod
  def setUpTestData(cls):
    populate_departments.populate()    

  def setUp(self):
    self.teacher1 = Teacher_profile.objects.create(first_name='Ethan',
    last_name='Ribera', department=Department.objects.get(name='Computer Science'))
    teacher_count = Teacher_profile.objects.all().count()

    self.teacher2 = Teacher_profile.objects.create(first_name='Gucci',
    last_name='Mane', department=Department.objects.get(name='Computer Science'))

    self.post1 = Post.objects.create(teacher=self.teacher1, overall_rating_num=0,
    difficulty_rating=5, grade_received='A', course_abbrv='CSC',
    course_num=333, compact_text='he was a good guy', post='collio',
    quarter_taken='Fall', year_taken=1999) 

    self.post2 = Post.objects.create(teacher=self.teacher1, overall_rating_num=2,
    difficulty_rating=5, grade_received='A', course_abbrv='CSC',
    course_num=666, compact_text='he was a good guy', post='collio',
    quarter_taken='Fall', year_taken=1999) 


    

    self.dpt = Department.objects.get(abbreviation='CSC')
    self.csc_666 = Course.objects.get(department=self.dpt, course_num=666)
    self.csc_333 = Course.objects.get(department=self.dpt, course_num=333)
    self.csc_222 = Course.objects.create(department=self.dpt, course_num=222)

  #simple test to check if teacher was saved to DB
  # don't be a Hater this is my first test
  def test_saving_to_db(self):
   
    teacher_count = Teacher_profile.objects.all().count()
    self.assertEqual(teacher_count, 2)

    teacher2 = Teacher_profile.objects.create(first_name='Gucci',
    last_name='Ribera', department=Department.objects.get(name='Computer Science'))

    teacher_count = Teacher_profile.objects.all().count()

    self.assertEqual(teacher_count, 3)

  #test just creates a teacher and post for that teacher and check if it saves
  def test_adding_post(self):
    
    post = Post.objects.create(teacher=self.teacher1, overall_rating_num=0,
    difficulty_rating=5, grade_received='A', course_abbrv='CSC',
    course_num=666, compact_text='he was a good guy', post='collio',
    quarter_taken='Fall', year_taken=1999)

    total_post_count = Post.objects.all().count()
    teacher_post_count = Post.objects.filter(teacher=self.teacher1).count()
    self.assertEqual(total_post_count, 3)
    self.assertEqual(teacher_post_count, 3)

  #test checks teacher attributes are set correctly
  def test_teacher_attributes(self):

    # these attrs are set in the overidden save method
    self.assertEqual(self.teacher1.slug, 'ethan-ribera')
    self.assertEqual(self.teacher1.full_name, 'Ethan Ribera')
    
    
    self.assertEqual(self.teacher1.evaluations, 2)

    self.assertEqual(self.teacher1.overall_rating, 1)
    self.assertEqual(self.teacher1.overall_difficulty, 5)
    
  def test_add(self):

    self.post2.delete()

    self.assertEqual(self.teacher1.evaluations, 1)
    self.assertEqual(self.teacher1.overall_difficulty, 5)

    self.post3 = Post.objects.create(teacher=self.teacher1, overall_rating_num=7,
    difficulty_rating=10, grade_received='A', course_abbrv='CSC',
    course_num=222, compact_text='he was a good guy', post='collio',
    quarter_taken='Fall', year_taken=1999)


    self.assertEqual(self.teacher1.evaluations, 2)
    self.assertEqual(self.teacher1.overall_difficulty, 7.5)
    self.assertEqual(self.teacher1.overall_rating, 3.5)

    self.assertTrue(self.csc_333 in self.teacher1.courses.all())
    self.assertFalse(self.csc_666 in self.teacher1.courses.all())
    self.assertTrue(self.csc_222 in self.teacher1.courses.all())



  def test_delete(self):

    self.post2.delete()

    self.assertEqual(self.teacher1.evaluations, 1)
    self.assertEqual(self.teacher1.overall_difficulty, 5)
    self.assertEqual(self.teacher1.overall_rating, 0)

    self.assertTrue(self.csc_333 in self.teacher1.courses.all())
    self.assertFalse(self.csc_666 in self.teacher1.courses.all())


  






  # changing overall and difficulty / changing teacher
  def test_update_post(self):
    self.post2.delete()
    self.assertEqual(int(self.teacher1.overall_difficulty), 5)
    self.post1.overall_rating_num=10
    self.post1.difficulty_rating = 10
    self.post1.save()



    
    self.assertEqual(self.teacher1.evaluations, 1)
    self.assertEqual(self.teacher1.overall_rating, 10)
    self.assertEqual(self.teacher1.overall_difficulty, 10)
    self.assertTrue(self.csc_333 in self.teacher1.courses.all())
    self.assertFalse(self.csc_666 in self.teacher1.courses.all())


    self.post1.course_num=666
    self.post1.save()
    self.assertEqual(self.teacher1.evaluations, 1)
    self.assertEqual(self.teacher1.overall_rating, 10)
    self.assertEqual(self.teacher1.overall_difficulty, 10)
    self.assertFalse(self.csc_333 in self.teacher1.courses.all())
    self.assertTrue(self.csc_666 in self.teacher1.courses.all())


    """
  # this is not implemented
  def test_change_teachers(self):
    # change teacher and check first teachers ratings
    self.post2.teacher = self.teacher2
    self.post2.save()


    # check second teachers ratings 
    self.assertEqual(self.teacher2.evaluations, 1)
    #self.assertEqual(self.teacher2.rating, 'A-')
    self.assertEqual(self.teacher2.overall_difficulty, 5)
    self.assertEqual(self.teacher2.overall_rating, 2)

    self.assertFalse(self.csc_333 in self.teacher2.courses.all())
    self.assertTrue(self.csc_666 in self.teacher2.courses.all())

    # check first teachers ratings
    teacher1 = Teacher_profile.objects.get(slug='ethan-ribera')
    self.assertEqual(teacher1.evaluations, 1)
    #self.assertEqual(teacher1.rating, 'A+')
    self.assertEqual(teacher1.overall_difficulty, 5)
    self.assertEqual(teacher1.overall_rating, 0)

    self.assertTrue(self.csc_333 in self.teacher1.courses.all())
    self.assertFalse(self.csc_666 in self.teacher1.courses.all()) 
    """

    """
  # this is not implemented
  def test_change_teachers(self):
    # change teacher and check first teachers ratings
    self.post2.teacher = self.teacher2
    self.post2.save()


    # check second teachers ratings 
    self.assertEqual(self.teacher2.evaluations, 1)
    #self.assertEqual(self.teacher2.rating, 'A-')
    self.assertEqual(self.teacher2.overall_difficulty, 5)
    self.assertEqual(self.teacher2.overall_rating, 2)

    self.assertFalse(self.csc_333 in self.teacher2.courses.all())
    self.assertTrue(self.csc_666 in self.teacher2.courses.all())

    # check first teachers ratings
    teacher1 = Teacher_profile.objects.get(slug='ethan-ribera')
    self.assertEqual(teacher1.evaluations, 1)
    #self.assertEqual(teacher1.rating, 'A+')
    self.assertEqual(teacher1.overall_difficulty, 5)
    self.assertEqual(teacher1.overall_rating, 0)

    self.assertTrue(self.csc_333 in self.teacher1.courses.all())
    self.assertFalse(self.csc_666 in self.teacher1.courses.all()) 
    """

    """
  # this is not implemented
  def test_change_teachers(self):
    # change teacher and check first teachers ratings
    self.post2.teacher = self.teacher2
    self.post2.save()


    # check second teachers ratings 
    self.assertEqual(self.teacher2.evaluations, 1)
    #self.assertEqual(self.teacher2.rating, 'A-')
    self.assertEqual(self.teacher2.overall_difficulty, 5)
    self.assertEqual(self.teacher2.overall_rating, 2)

    self.assertFalse(self.csc_333 in self.teacher2.courses.all())
    self.assertTrue(self.csc_666 in self.teacher2.courses.all())

    # check first teachers ratings
    teacher1 = Teacher_profile.objects.get(slug='ethan-ribera')
    self.assertEqual(teacher1.evaluations, 1)
    #self.assertEqual(teacher1.rating, 'A+')
    self.assertEqual(teacher1.overall_difficulty, 5)
    self.assertEqual(teacher1.overall_rating, 0)

    self.assertTrue(self.csc_333 in self.teacher1.courses.all())
    self.assertFalse(self.csc_666 in self.teacher1.courses.all()) 
    """

