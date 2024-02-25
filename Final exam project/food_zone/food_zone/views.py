from django.shortcuts import render
from store.models import Food,Category
# Create your views here.


def home(request):
    if request.method == 'POST':
        cata = request.POST.get('category')
        catagory = Category.objects.get(category_name=cata)
        all_food = Food.objects.filter(category=catagory)

    else:
       all_food = Food.objects.all()
    
    catagories = Category.objects.all()
   
    return render(request,'index.html',{'items':all_food,'catagories': catagories})