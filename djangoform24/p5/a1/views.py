from django.shortcuts import render

from .import forms
# Create your views here.

def form(request):
    
    return render (request,'from.html')
    
    
    
def about(request):
    if request.method == 'POST':
        print(request.POST)
        email = request.POST.get('username')
        return render (request,'about.html',{'email':email})
    
    
    return render (request,'about.html')



 
def django_form(request):
    if request.method=="POST":
        form = forms.Myform(request.POST,request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            file = form.cleaned_data['file']
            with open('a1/uploads/' + file.name, 'wb+') as desti: 
              for cuck in file.chunks():
                 desti.write(cuck)
        return render(request,'djangoform.html',{'form':form})
    else:
      form = forms.Myform()
      return render(request,'djangoform.html',{'form':form})
    
    
def st(request):
    if request.method=="POST":
        form = forms.Student(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        return render(request,'st.html',{'form':form})
    else:
      form = forms.Student()
      return render(request,'st.html',{'form':form})
    