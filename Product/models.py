from django.db import models
from Supplier.models import sTable

# Create your models here.


class pTable(models.Model):
    productID = models.BigAutoField(primary_key=True)
    supplierID = models.ForeignKey(sTable, on_delete=models.CASCADE)
    productPrice = models.DecimalField(max_digits=10, decimal_places=2)
    productName = models.CharField(max_length=30) 