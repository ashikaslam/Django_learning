from django.db import models

# Create your models here.

class Students(models.Model):
    name = models.CharField(max_length=30)
    roll = models.IntegerField(primary_key = True)
    addrress = models.TextField()

    def __str__(self) -> str:
        return self.name