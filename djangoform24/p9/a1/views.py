from django.shortcuts import render,redirect,HttpResponse
from.import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import PasswordChangeForm # we use it when we have our old pass
from django.contrib.auth.forms import SetPasswordForm # we use it when we  do not have our old pass
from django.contrib.auth import update_session_auth_hash # we use it  when  change ourpass and pass is in hass formate
# Create your views here.


def home(request):return render(request,'base.html')
    

def signup(request):

    if request.method == "POST":
        fom = forms.Register_user_form(request.POST)
        print(1001)
        if fom.is_valid():
            messages.success(request,'account created successfully')
            print(fom.cleaned_data)
            fom.save(commit=True)
            return render(request,'signup.html',{"form":fom})
    else:
      fom = forms.Register_user_form
    return render(request,'signup.html',{"form":fom})



def logiN(request):
   
      if request.method=='POST':
              fom = AuthenticationForm(request,data=request.POST)
              if fom.is_valid():
                name = fom.cleaned_data['username']
                pas = fom.cleaned_data['password']
                user = authenticate(username = name,password=pas) # here we are chacking that the user is in the database 
                # jodi kono non fiedl error thake tahole ekhan thek html file e jabe
                if user is not None:
                    login(user=user,request=request)
                    return redirect('profile')
                
      else:
        fom = AuthenticationForm()
      return render(request,'login.html',{'form':fom})
      
      # return HttpResponse("<h3>soryy wrong info</h3>")


def profile(request):
    user = request.user
    if not user.is_authenticated: return redirect('signup')
    return render(request,'profile.html')




def user_logout(request):
    user = request.user
    if not user.is_authenticated: return redirect('signup')
    logout(request)
    return redirect('login')
            

  

def change_pass(request): # we cna change pass with odl password
    if request.method=='POST':
        print('hello in 99 ')
        fom = PasswordChangeForm(user=request.user,data = request.POST) ## if the form is not valid i want to pass or show erros mangess
        print('hello in 990 ')
        print(request.POST)
        if fom.is_valid():
            fom.save()
            print('hello in 100 ')
            update_session_auth_hash(request,fom.user)
            return redirect('profile')
        
    else:  fom = PasswordChangeForm(user=request.user)
    return render(request,'passchange.html',{'form':fom})




def chapass_without_old_pss(request):
    if request.method=='POST':
        fom = SetPasswordForm(user=request.user,data = request.POST)
        if fom.is_valid():
            fom.save(commit=True)
            update_session_auth_hash(request,fom.user)
            return redirect('profile')

    else: fom =SetPasswordForm(user=request.user)
    return render(request,'passchange.html',{'form':fom})

    


def change_user_data(request):
    if request.method == 'POST':
        fom = forms.User_data_chage(instance=request.user,data = request.POST)
        if fom.is_valid():
            fom.save()
            return redirect('profile')


    else:fom = forms.User_data_chage(instance=request.user)
    return render(request,'user_data_change.html',{'form':fom})
