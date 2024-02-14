from django.db import models
from django.contrib.auth.models import User
from . constrains import ACCOUNT_TYPE ,GENDER
# Create your models here.


class Accounts(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE,related_name='account')
    account_type =models.CharField(max_length=10,choices=ACCOUNT_TYPE)
    account_no = models.IntegerField(unique=True)
    birth_date =models.DateField(null=True,blank = True)
    gender = models.CharField(max_length=10,choices = GENDER)
    initial_deposite_date=models.DateTimeField(auto_now_add=True)
    balance =models.DecimalField( max_digits=12, decimal_places=2,default=0.0)
    def __str__(self):
        return str(self.account_no)



class  UserAddress(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE,related_name='address')
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length= 100)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=100)
    def __str__(self):
        return self.user.email
    
