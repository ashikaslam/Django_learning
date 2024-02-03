from django.db import models

# Create your models here.





class Book(models.Model):
    CATAGORY = (('f','funny'), ('h','horor'), ('s','sifi'), ('j','jock'))
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 30)
    cata = models.CharField(max_length = 30,choices = CATAGORY )
    author = models.CharField(max_length = 20)
    first_pub = models.DateTimeField(auto_now_add = True)
    last_pub = models.DateTimeField(auto_now = True)

    def __str__(self):return self.name
