

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):

    def create_user(self, mobile_number, password,name,email ):
        if not mobile_number:
            raise ValueError("Mobile number is required.")
        if not password:
            raise ValueError("password is required.")
        if not name:
            raise ValueError("name is required.")
        if not email:
            raise ValueError("email is required.")
       
        
        user = self.model(
                           mobile_number=mobile_number,
                           username=mobile_number,
                           name=name,
                           email=email,
                         )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, mobile_number, password,name,email):
        user = self.create_user(mobile_number, password, name,email)
        user.is_active = True
        user.account_type = 'administrator'
        user.profile_picture = 'static_files/images/admin_image.png'
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


ACCOUNT_CHOICES = [
    ('student', 'student'),
    ('instructors', 'instructors'),
    ('administrator', 'administrator'),
    ('administrator_instructor', 'administrator_instructor'),
    
    ]

class User(AbstractUser):
    mobile_number = models.CharField(max_length=11, null=False, unique=True)
    otp = models.CharField(max_length=6,blank=True)
    name=models.CharField( max_length=50, blank=False)
    email =models.CharField(max_length=100,blank=False)
    email_is_varifaied=models.BooleanField(default=False)
    flag=models.BooleanField(default=False)
    account_type=models.CharField(choices =ACCOUNT_CHOICES,default='student',max_length=35)
    profile_picture=models.ImageField(upload_to='images/user_profile_Pic',default='static_files/images/student_image.jpeg')
    USERNAME_FIELD = "mobile_number"
    REQUIRED_FIELDS = ['name','email']
    objects = UserManager()

    def __str__(self) -> str:
        return f"{self.name}"
    



GENDER = (
    ('MALE', 'MALE'),
    ( 'FEMALE', 'FEMALE'),
   
)


class ApplicationsForinstructors(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=17)
    gender = models.CharField(choices=GENDER,max_length=10) 
    email = models.EmailField()
    educations = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    applicatoins_date = models.DateTimeField(auto_now=True)
    aproved = models.BooleanField(default=False)

    class Meta:
        ordering = ['applicatoins_date']
    def __str__(self):
        return f"{self.user.name}"



class InstructorsProfile(models.Model):
    name = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='instructor_profile')
    phone_number = models.CharField(max_length=17)
    gender = models.CharField(choices=GENDER,max_length=10)  
    educations = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    ragistraions_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.name}"
   
    



    


