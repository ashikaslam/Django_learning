from typing import Any
from django.http import HttpResponse
from django.shortcuts import render,redirect
from . import forms,models
from django .views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import FormView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.

# def home(request):
#     return render(request,'base.html')

class Home(TemplateView):
    template_name  ='base.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
       context_data = super().get_context_data(**kwargs)
       context_data = {'name':'aslam','roll':570963}
       print(kwargs)
       context_data.update(kwargs)
       return context_data


    




# def store_book(request):
#     if request.method == "POST":
#         fom = forms.Book_store_form(request.POST)
#         if fom.is_valid():
#             print(fom.cleaned_data)
#             fom.save(commit=True)




#     fom = forms.Book_store_form
#     return render(request,'store.html',{'form':fom})


# class Store_book(FormView):
#     template_name = 'store.html'
#     form_class = forms.Book_store_form
#     success_url = reverse_lazy('show')

#     def form_valid(self, form: Any) -> HttpResponse:
#        print(form.cleaned_data)
#        if form.is_valid():form.save()
#        return redirect('store')


class Store_book(CreateView):
    template_name = 'store.html'
    form_class = forms.Book_store_form
    success_url = reverse_lazy('show')





# def show_book(request):
#    all_book = models.Book.objects.all()
#    for i in all_book:
#        print(i)

#    return render(request,'show.html',{'data':all_book})




class Show_book(ListView):
    model = models.Book
    template_name  ='show.html'
    # context_object_name = 'data'
    # ordering = ['-id']
    # def get_template_names(self):
    #     pass # with this funtion we can render several template according to  many stuffs
        
        
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
       context_data = super().get_context_data(**kwargs)
       all_books = models.Book.objects.order_by('name')
       context_data = {'data':all_books}
       return context_data
    


class detial_for_a_book(DetailView):
    template_name = 'details.html'
    model = models.Book
    context_object_name = 'data'
    pk_url_kwarg = 'id'



# def delete(request,roll):
#     book = models.Book.objects.get(pk = roll).delete()
#     return redirect('home') ## this takes a url not a template
    

class Edit(UpdateView):
    model= models.Book
    template_name = 'edit.html'
    form_class = forms.Book_store_form
    success_url = reverse_lazy('show')


# def edit(request,roll):
      
#     book  = models.Book.objects.get(pk = roll)
#     if request.method == "POST":
#         print('hello1')
#         fom = forms.Book_store_form(request.POST,instance=book)
#         if fom.is_valid():
#             print(fom.cleaned_data)
#             fom.save(commit=True)
#             return redirect('home')
#     print('hello1')
#     fom = forms.Book_store_form(instance=book)
#     return render(request,'edit.html',{'form':fom})


class Edit(UpdateView):
    model= models.Book
    template_name = 'edit.html'
    form_class = forms.Book_store_form
    success_url = reverse_lazy('show')

class Delete(DeleteView):
    model= models.Book
    template_name = "delecon.html"
    success_url = reverse_lazy('show')
