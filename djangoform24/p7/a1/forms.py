from typing import Any
from django import forms
from . import models






class Stufrom(forms.ModelForm):
    class Meta:

        model = models.Student  # we have to name it model nothin else
        fields = '__all__'
       # fields =['name']
        #exclude=['name']

        labels={ 
            'roll':'your roll'   
        }

        widgets={


        }

        help_texts={

'roll':'enter ur roll'

        }






       




















































































    