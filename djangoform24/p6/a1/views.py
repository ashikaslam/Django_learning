from django.shortcuts import render,redirect
from . import models
# Create your views here.


def home(request):
   st = models.Students.objects.all()
   for i in st:print(i)
   return render(request,'home.html',{'data':st})




def delete(request,rol):
   st = models.Students.objects.get(pk=rol).delete()
   return redirect('home')
   