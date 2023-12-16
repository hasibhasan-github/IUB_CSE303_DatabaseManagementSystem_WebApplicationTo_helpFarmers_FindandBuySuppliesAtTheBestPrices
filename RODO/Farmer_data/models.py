# from django.db import models

#  # Create your models here.

# class Farmer(models.Model):
#       fid = models.IntegerField()
#       fname = models.CharField(max_length=40)
#       femail = models.EmailField(max_length=30)

from django.db import models

class Farmer(models.Model):
    # Define your fields here
    field_id = models.IntegerField()
    f_name = models.CharField(max_length=40)
    f_email = models.EmailField(max_length=30)
   
