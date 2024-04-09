from django.db import models

# Create your models here.


class ContactUs(models.Model):
    name = models.CharField( max_length=50)
    phone = models.CharField(max_length=15)
    problem = models.TextField()


    class Meta:
        verbose_name = "ContactUs"
        verbose_name_plural = "ContactUs"


    def __str__(self) -> str:
        return self.name