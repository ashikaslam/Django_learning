from django.shortcuts import render,redirect
from . import forms
from django.views.generic.edit import FormView
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.views import LoginView,LogoutView
from django.views import View
# Create your views here.

def register_user(request):# functons base register viwe
    if request.method == 'POST':
         fom = forms.User_register_form(request.POST)
         if fom.is_valid():
          user =  fom.save()
    else:
        fom = forms.User_register_form
        return render(request,'f1.html',{'form':fom})
    return render(request,'f1.html',{'form':fom})



class User_register_FormView(FormView): # class based viwe fo user register 
    template_name = "f1.html"
    form_class = forms.User_register_form
    success_url ='home'
   # success_url = reverse_lazy()

    def form_valid(self, form): # it is autometic called when the from is valied
        user =  form.save()
        login(self.request, user)
        return super().form_valid(form)




#>>>>>>>>>>>>>>>>>>> login>>>>>>>>>>>>>>>>>>
    
def user_login(request):
    if request.method == 'POST':
        form = forms.User_Login_form(request.POST)
        if form.is_valid():
          username = form.cleaned_data['username']
          password = form.cleaned_data['password']
          user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    
        else: 
           
            return redirect('login')
    else:
        form = forms.User_Login_form()
        return render(request, 'login.html',{'form':form})
    

class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = "login.html"
    def get_success_url(self):
        return reverse_lazy('home') 
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))




#>>>>>>>>>>>>>>>>>>> logout>>>>>>>>>>>>>>>>>>

def user_logout(request):
    logout(request)
    return redirect('home')


class UserLogoutView(LogoutView):
    def get_next_page(self):
        if self.request.user.is_authenticated:
            logout(self.request)
            return reverse_lazy('login')  # Assuming 'login' is the name of your login page
        else:
            return reverse_lazy('home')  # Redirect to home if the user is not authenticated

# >>>>  profile>>>>>>>>>>>

class show_profile(View):
    template_name = 'profile.html'
    def get(self, request):
        form = forms.User_profile_update(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form =forms.User_profile_update(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the user's profile page
        return render(request, self.template_name, {'form': form})
    



