from django.db import models
from django.contrib.auth.models import User
from store.models import Food,Category
# Create your models here.
class Cart_item(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     food= models.ForeignKey(Food,on_delete=models.CASCADE)
     quantity=models.IntegerField()

     def sub_stotal(self):return self.quantity*self.food.price
     def __str__(self) -> str:
          return self.food.food_name