from django.shortcuts import render

# Create your views here.

arr = [12,3,4,5 ,7]

dic = {'num':12,'name':'aslam','word':'hello world itz 2024'}

def home(request):
    return render(request,'index1.html',context={'num':arr})


def filter(request):
    return render (request,'filter.html', {'num':12,'name':'aslam','word':'hello world itz 2024'})