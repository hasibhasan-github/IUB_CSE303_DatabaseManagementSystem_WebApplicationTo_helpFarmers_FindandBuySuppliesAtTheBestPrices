from django.db import models
from django import forms


# Create your models here.

# Widgets 


class CustomForm(forms.Form):
    custom_field = forms.CharField()



class Test(models.Model):
    fname = models.CharField(max_length=30)

    def __str__ (self):
        return f"{self.fname}"


class bug(models.Model):
    id = models.IntegerField(primary_key=True, default=784)
    user = models.CharField(max_length=30, default='Hasib')
