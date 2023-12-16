from django.db import models
from Supplier.models import sTable
from Product.models import pTable
from Farmer.models import fTable

# Create your models here.


class oTable(models.Model):
    orderId = models.BigAutoField(primary_key=True)
    supplierID = models.ForeignKey(sTable, on_delete=models.CASCADE)
    productID = models.ForeignKey(pTable, on_delete=models.CASCADE)
    farmerID = models.ForeignKey(fTable , on_delete= models.CASCADE)  
    orderDate = models.DateField()
    quantity = models.PositiveIntegerField()
    totalPrice = models.DecimalField(max_digits=10, decimal_places=2) 
    address = models.CharField( max_length=500)