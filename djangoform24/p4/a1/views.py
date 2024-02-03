from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'index.html',context={'author':"ahikaslam"})


def about(request):
     return render(request,'about.html',context={'num':12})