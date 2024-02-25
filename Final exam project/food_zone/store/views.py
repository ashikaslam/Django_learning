from django.shortcuts import render,redirect
from.models import Food,Category
# Create your views here.


# functon for searchr

def search_feature(request):
    if request.method == 'POST':
        search_query = request.POST['search_query']
        all_food = Food.objects.filter(food_name__contains=search_query)
    catagories = Category.objects.all()
    return render(request,'index.html',{'items':all_food,'catagories':catagories})
    


def pro_detials(request,pk):
    yes_ase = Food.objects.filter(pk=pk).exists()
    if yes_ase:
       food =  Food.objects.get(pk=pk)
       return render(request,'food.diteals.html',{'food':food})
    return redirect('home')