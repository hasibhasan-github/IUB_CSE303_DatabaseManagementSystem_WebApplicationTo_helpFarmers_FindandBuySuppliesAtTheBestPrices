from django.db import models

# Create your models here.



class Test(models.Model):
    fname = models.CharField(max_length=30)


    def __str__ (self):
        return f"{self.fname}"
    
