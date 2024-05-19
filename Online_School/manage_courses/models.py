from django.db import models
from user_accounts_manager.models import InstructorsProfile,User
# Create your models here.

COURSE = (
    ('MATH', 'Mathematics'),
    ('ENG', 'English'),
    ('SCI', 'Science'),
    ('HIST', 'History'),
    ('CS', 'Computer Science'),
    ('BIO', 'Biology'),
    ('CHEM', 'Chemistry'),
    ('PHY', 'Physics'),
    ('PY', 'Python Programming'),
    ('CPP', 'C++ Programming'),
    ('DSL', 'Data Structures and Algorithms'),
    ('GO', 'Go Programming'),
    ('JAVA', 'Java Programming'),
)



class Course(models.Model):
    instructor = models.ForeignKey(InstructorsProfile,on_delete=models.CASCADE,related_name="my_coures")
    title = models.CharField(max_length=150)
    description = models.TextField()
    cover_picture=models.ImageField(upload_to='images/course_cover_pic',default='static_files/images/default_coures_image.png',blank=True)
    catagory = models.CharField(choices =COURSE,max_length=30)
    enrolled_students = models.ManyToManyField(User,related_name="coures_i_took",blank=True)
   

