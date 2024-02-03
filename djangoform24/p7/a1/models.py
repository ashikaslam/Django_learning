from django.db import models

# Create your models here.

class Comon_info(models.Model):
     name = models.CharField(max_length=20)
     addr = models.CharField(max_length=200)

     class Meta:
         abstract = True

class Student(Comon_info):
    roll = models.IntegerField(primary_key=True)
    father_name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name


class Teacher(Comon_info):
    salary = models.IntegerField()
    

    def __str__(self) -> str:
        return self.name




class Employee(models.Model):
    name = models.CharField(max_length=20)
    addr = models.CharField(max_length=200)
    degicnaton=models.CharField(max_length=200)


class Maneger(Employee):
    take_int = models.BooleanField()
    hiring = models.BooleanField()




# proxy model
    
class Friends(models.Model):
    name = models.CharField(max_length=20)
    Calas = models.CharField(max_length=20)
    present = models.BooleanField()
    roll = models.IntegerField(null = True)
    

    class Meta:
       
        ordering = ['roll']


class Me(Friends):
    class Meta:
        proxy = True
        ordering = ['roll']

# one to one

class People(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    addr = models.CharField(max_length=200)

    def __str__(self):return self.name

class Passport(models.Model):
    user_id = models.OneToOneField(to=People,on_delete = models.CASCADE,related_name='pas')
    pasNUM = models.IntegerField(primary_key = True)
    total_page = models.IntegerField()
        


# one to many
    
# we will use the People class for it
    
class Post(models.Model):
    user = models.ForeignKey(People,on_delete = models.CASCADE) # here user is 1 but post can be many
    titel = models.CharField(max_length= 100)
    discrip = models.TextField()




# many to many rel


class Stu(models.Model):
    roll =models.IntegerField(primary_key = True)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    def __str__(self):return self.name

class Tec(models.Model):
    stuednts = models.ManyToManyField(Stu,related_name='teachers') # we can not use ondelete here   and here we will store stu oject in a list

    name = models.CharField(max_length=20)
    sub = models.CharField(max_length=20)
    def __str__(self):return self.name

    def stu_List(self):
        x = ','.join([str(i) for i in self.stuednts.all()])
        return x
    