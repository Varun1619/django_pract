from dataclasses import fields
from pyexpat import model
#ModelForm helps to create a form fro the respective Model

from django.forms import ModelForm
from .models import form_pract

class form_practForm(ModelForm):
    class Meta:
        model = form_pract
        #specifies the model for which we want to create a form

        fields = "__all__"
        #Specifies the fields for which we want to create the form