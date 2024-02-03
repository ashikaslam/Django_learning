from typing import Any
from django import forms


# widget hepl us to make django form to html input
class Myform(forms.Form):
    name=forms.CharField(max_length=30,required=False)
    eamil =  forms.EmailField(max_length=50,required=False)
    age = forms.IntegerField()
    check = forms.BooleanField()
    bith_day = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    choize = [('s','small'),('l','lager')]
    size = forms.ChoiceField(choices= choize,widget=forms.RadioSelect)
    choize_1 = [('s','sosa'),('l','lebu'),('g','gaxor')]
    pizza = forms.MultipleChoiceField(choices=choize_1,widget=forms.CheckboxSelectMultiple)
    file = forms.FileField()



class Student(forms.Form):
   name=forms.CharField(max_length=30,required=False)
   eamil =  forms.EmailField(max_length=50,required=False)



   def clean(self):
      all_data =  super().clean()
      valname = all_data['name']
      if len(valname)<10:raise forms.ValidationError("name must be atleast 10 char")

       




















































































    