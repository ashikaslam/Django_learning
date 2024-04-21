from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):

    def create_user(self, mobile_number, password, address=""):
        if not mobile_number:
            raise ValueError("Mobile number is required.")
        user = self.model(mobile_number=mobile_number, address=address,username=mobile_number)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, mobile_number, password, address=""):
        user = self.create_user(mobile_number, password, address)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



class User(AbstractUser):
    mobile_number = models.CharField(max_length=13, null=False, unique=True)
    address = models.CharField(max_length=255, blank=True)
    otp = models.CharField(max_length=6,blank=True)
    USERNAME_FIELD = "mobile_number"
    REQUIRED_FIELDS = []
    objects = UserManager()
