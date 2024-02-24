from django.shortcuts import render,redirect
from.forms import Rgister_form,Login_form
from django.contrib.auth import logout,login
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from cart.views import get_or_create_session
from cart.models import Cart,CartItem
# Create your views here.

def register(request):
         if request.method=="POST":
              
               form = Rgister_form(request.POST)
               if form.is_valid():
                     user = form.save()
                     the_sesson_id = get_or_create_session(request)

                     if user is not None:
                        login(request, user)
                     else: return redirect('register')
                     
                     login(request,user)
                     if request.user.is_authenticated:
                           
                           cart_id = Cart.objects.filter(cart_id=the_sesson_id).exists() # it return a bool value
                           if cart_id:
                            my_card = Cart.objects.get(cart_id=the_sesson_id)
                            cart_items = CartItem.objects.filter(cart=my_card)
                            for i in cart_items:
                               i.user =  user
                               i.save()
                     return redirect('store')
         else:form = Rgister_form()
         return render(request, 'accounts/register.html',{'form':form})
   
                
    

   

def profile(request):
    return render(request, 'accounts/dashboard.html')


def user_login(request):
   
    if request.method == "POST":
                usernem = request.POST.get('username')
                passwrd = request.POST.get('password')
                user = authenticate(username=usernem,password=passwrd)

                sessionId = get_or_create_session(request)

                if user is not None:
                   login(request, user)
                
                else: return redirect('login')
            
               
                cart_id = Cart.objects.filter(cart_id=sessionId).exists() # it return a bool value
                if cart_id:
                         my_card = Cart.objects.get(cart_id=sessionId)
                       #  print('ase>>> adn id', my_card,cart_id)
                         cart_items = CartItem.objects.filter(cart=my_card)
                         for i in cart_items:
                               print(i.product.product_name)
                               i.user =  user
                               i.cart= None
                               i.save()
                         my_card.delete()
                        
                return redirect('profile')
        
    return render(request,'accounts/signin.html')




def UserLogoutView(request): 
     logout(request)
     return redirect('store')