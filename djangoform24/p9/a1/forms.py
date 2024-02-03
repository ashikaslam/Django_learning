from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms



class Register_user_form(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'required': True}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'required': True}))
    class Meta:
        model = User
        fields =  ['username', 'first_name', 'last_name', 'email']


class User_data_chage(UserChangeForm):
    password=None
    class Meta:
        model = User
        fields =  ['first_name', 'last_name', 'email']



