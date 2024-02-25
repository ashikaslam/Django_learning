from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
     category_name = models.CharField(max_length=50,unique=True)
     category_img =models.ImageField(upload_to = 'photos/categories', blank = True)
     slug = models.SlugField(max_length= 100, unique = True,default=None)

     def __str__(self) -> str:
          return self. category_name


class Food(models.Model):
    food_name = models.CharField(max_length=50)
    price = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    food_img =models.ImageField(upload_to = 'photos/foodes', blank = True)
    descriptons=models.TextField()
    slug = models.SlugField(max_length= 100, unique = True,default=None)
    def __str__(self) -> str:
          return self.food_name






