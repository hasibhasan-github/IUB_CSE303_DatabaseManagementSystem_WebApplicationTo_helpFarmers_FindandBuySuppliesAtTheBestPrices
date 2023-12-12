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
    


class TestProduct(models.Model):
    productID = models.BigAutoField(primary_key=True)
    supplierID = models.IntegerField(null=True)
    productPrice = models.DecimalField(max_digits=10, decimal_places=2)
    productName = models.CharField(max_length=30) 
