import email
from statistics import mode
from django.db import models

# Create your models here.

class form_pract(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    contact = models.CharField(max_length=200)
    message = models.TextField(max_length=300, blank=True)

    def __str__(self):
        return self.name