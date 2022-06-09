from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from .models import form_pract

class form_practForm(ModelForm):
    class Meta:
        model = form_pract
        fields = "__all__"