from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login,logout
# Create your views here.



def sign_up(request):
    if request.method=="POST":
         form = RegistrationForm(request.POST) 
         print('hello')
         if form.is_valid():
             user = form.save()
             login(request,user)
             return redirect('home')
        
    else:
        form = RegistrationForm()    


    return render (request,'register.html',{'form':form})


def log_in(request):
   if request.method=='POST':
       username = request.POST['username']
       password = request.POST['password']
       user = authenticate(username= username, password= password)
       if user is not None:
           login(request,user)
           return redirect('home')

   return render(request,'login.html')




def log_out(request):
    logout(request)
    return redirect('home')


