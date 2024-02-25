from django.shortcuts import render, redirect
from store.models import Product
# Create your views here.
from .models import Cart, CartItem

def get_or_create_session(request):
        if not request.session.session_key:
            request.session.create()
        return request.session.session_key

def cart(request):
    if request.user.is_authenticated: # loing hole
         print('inside 101')
         user = request.user
         total_price = 0
         cart_items = CartItem.objects.filter(user=user)
         total_price = 0
         for i in cart_items:total_price+=i.sub_total()
         total_price+= total_price*0.10
         total_price= int(total_price)
         if len(cart_items)==0:
              cart_items=[]
              return render(request,'cart/cart.html',{"cart_items":cart_items})
         return render(request,'cart/cart.html',{"cart_items":cart_items,"total_price":total_price})
    
    else:
        session_id = get_or_create_session(request)
        cart_id = Cart.objects.filter(cart_id=session_id).exists() # it return a bool value
        if cart_id:
            my_card = Cart.objects.get(cart_id=session_id)
        
            total_price = 0
            cart_items = CartItem.objects.filter(cart=my_card)
            for i in cart_items:total_price+=i.sub_total()
            total_price+=(total_price*0.1)
            total_price= int(total_price)
        
            return render(request,'cart/cart.html',{"cart_items":cart_items,"total_price":total_price})
        else:
            cart_items=[]
            return render(request,'cart/cart.html',{"cart_items":cart_items})

    

def removeall_form_cart(request, product_id):
     if request.user.is_authenticated: 
         product = Product.objects.get(id=product_id)
         user = request.user
         cart_item = CartItem.objects.filter(user=user,product=product).exists()
         if cart_item:
                item = CartItem.objects.get(user=user,product=product)
                item.delete()

     else:
        product = Product.objects.get(id=product_id)
        session_id = get_or_create_session(request)
        cart_id = Cart.objects.filter(cart_id = session_id).exists()
        if cart_id:
            cartid = Cart.objects.get(cart_id = session_id)
            cart_item = CartItem.objects.filter(cart = cartid,product=product).exists()
            if cart_item:
                item = CartItem.objects.get(cart = cartid,product=product)
                item.delete()
     return redirect('cart')
    




def add_to_cart(request, product_id):
    if request.user.is_authenticated: # loing hole
        print('login>>')
        product = Product.objects.get(id=product_id)
        user = request.user
        cart_item = CartItem.objects.filter(user= user,product=product).exists()
        if cart_item:
                item = CartItem.objects.get(user= user,product=product)
                item.quantity +=1
                item.save()
        else :
                item = CartItem.objects.create(
                    user= user,
                    product = product,
                    quantity = 1
                )
                item.save()
      
    
    else:  # login na hole
        print('login na >>>')
        product = Product.objects.get(id=product_id)
        sessionId = get_or_create_session(request)
        
        cart_id = Cart.objects.filter(cart_id = sessionId).exists()
        if  not cart_id:
            cart = Cart.objects.create(
            cart_id = sessionId)
            cart.save()

        cartid = Cart.objects.get(cart_id = sessionId)
        cart_item = CartItem.objects.filter(cart = cartid,product=product).exists()
        if cart_item:
                item = CartItem.objects.get(cart = cartid,product=product)
                item.quantity +=1
                item.save()

        else :
                item = CartItem.objects.create(
                    cart = cartid,
                    product = product,
                    quantity = 1)
                item.save()

        
        



    return redirect('cart')






def remove_form_cart(request, product_id):
    
     product = Product.objects.get(id=product_id)
     if request.user.is_authenticated:
        user = request.user
        cart_item = CartItem.objects.filter(user= user,product=product).exists()


        if cart_item:
                item = CartItem.objects.get(user= user,product=product)
                item.quantity -=1
                if item.quantity <1: item.delete()
                else: item.save()
          


     else:
        session_id = get_or_create_session(request)
        cart_id = Cart.objects.filter(cart_id = session_id).exists()

        if cart_id:
            cartid = Cart.objects.get(cart_id = session_id)
            cart_item = CartItem.objects.filter(cart = cartid,product=product).exists()
            if cart_item:
                item = CartItem.objects.get(cart = cartid,product=product)
                item.quantity -=1
                if item.quantity <1: item.delete()
                else: item.save()

     return redirect('cart')





def make_payment(request):
     user = request.user
     if user.is_authenticated:
         user = request.user
         cart_items = CartItem.objects.filter(user=user)
         total_price = 0
         for i in cart_items:total_price+=i.sub_total()
         total_price+= total_price*0.10
         total_price= int(total_price)
         return render(request,'cart/payment.html',{'all_products':cart_items,'total':total_price})

     else:
          return redirect('login')
     
     return render(request,'cart/payment.html')