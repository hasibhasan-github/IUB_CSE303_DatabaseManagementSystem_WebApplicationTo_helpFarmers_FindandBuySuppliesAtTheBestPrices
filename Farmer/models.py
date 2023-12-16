from django.db import models

# Create your models here.
class fTable(models.Model):
    farmerID = models.BigAutoField(primary_key=True, unique=True)
    email = models.EmailField('Email address', unique=True)
    fname = models.CharField(max_length=30, blank=True)
    lname = models.CharField(max_length=30, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    house = models.CharField(max_length=50, blank=True)
    street = models.CharField(max_length=50, blank=True)
    thana = models.CharField(max_length=50, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    city = models.CharField(max_length=50, blank=True)
    contactnumber = models.CharField(max_length=15, blank=True)



class Cart(models.Model):
    supplier = models.CharField(max_length=255)
    product = models.CharField(max_length=255)
    quantity = models.IntegerField()
    totalPrice = models.DecimalField(max_digits=10, decimal_places=2)

    

