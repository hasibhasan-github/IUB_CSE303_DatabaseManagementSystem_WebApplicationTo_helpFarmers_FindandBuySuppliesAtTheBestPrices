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
    prod_ID = models.BigAutoField(primary_key=True)
    supp_ID = models.IntegerField(null=True)
    prod_price = models.DecimalField(max_digits=10, decimal_places=2)
    prod_name = models.CharField(max_length=30)

    labels = {
            'prod_name': 'Product Name: ',
        }
