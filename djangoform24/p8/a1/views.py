from django.shortcuts import render,redirect
from . import forms,models

# Create your views here.

def home(request):
    return render(request,'base.html')






def store_book(request):
    if request.method == "POST":
        fom = forms.Book_store_form(request.POST)
        if fom.is_valid():
            print(fom.cleaned_data)
            fom.save(commit=True)




    fom = forms.Book_store_form
    return render(request,'store.html',{'form':fom})


def show_book(request):
   all_book = models.Book.objects.all()
   for i in all_book:
       print(i)

   return render(request,'show.html',{'data':all_book})






def delete(request,roll):
    book = models.Book.objects.get(pk = roll).delete()
    return redirect('home') ## this takes a url not a template
    


def edit(request,roll):
      
    book  = models.Book.objects.get(pk = roll)
    if request.method == "POST":
        print('hello1')
        fom = forms.Book_store_form(request.POST,instance=book)
        if fom.is_valid():
            print(fom.cleaned_data)
            fom.save(commit=True)
            return redirect('home')
    print('hello1')
    fom = forms.Book_store_form(instance=book)
    return render(request,'edit.html',{'form':fom})



