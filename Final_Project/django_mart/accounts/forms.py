
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm  
from django.forms.widgets import PasswordInput

class Rgister_form(UserCreationForm):
     class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            ]

        widgets = {
            "password1":PasswordInput(),
            "password2":PasswordInput(),
        }

from django import forms 
  
# creating a form 
class Login_form(forms.Form): 
    user_name = forms.CharField()
    pass_word = forms.CharField()