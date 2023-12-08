from django.db import models

# Create your models here.
class Set_Price(models.Model):
    Upper_Price = models.IntegerField(default=0)
    Lower_Price = models.IntegerField(default=0)

    def __str__(self):
        return f'Upper Price is {self.Upper_Price} and Lower Price is {self.Lower_Price}'