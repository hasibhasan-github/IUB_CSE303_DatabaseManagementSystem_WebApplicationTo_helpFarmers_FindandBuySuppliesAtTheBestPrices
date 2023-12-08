from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_supplier= models.BooleanField('Is supplier', default=False)
    is_farmer = models.BooleanField('Is farmer', default=False)
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
    supplierType = models.CharField(max_length=50, blank=True)
    userType = models.CharField(max_length=20, blank=True, default="Supplier")