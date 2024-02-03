from django import forms
from . import models

class Book_store_form(forms.ModelForm):
    class Meta:
        model = model = models.Book
        fields = "__all__"