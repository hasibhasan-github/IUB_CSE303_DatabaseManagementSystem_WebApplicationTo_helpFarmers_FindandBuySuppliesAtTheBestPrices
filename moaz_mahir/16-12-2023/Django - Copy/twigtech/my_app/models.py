from django.db import models

# Create your models here.
class Supplier(models.Model):
    # define the fields for your model
    supplierID = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    contactNumber = models.CharField(max_length=20)
    supplierType = models.CharField(max_length=100)
    
class Farmer(models.Model):
    # define the fields for your model
    farmerID = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    contactNumber = models.CharField(max_length=20)
    cropType = models.CharField(max_length=100)
    livestockType = models.CharField(max_length=100)
    
class Product(models.Model):
    # define the fields for your model
    ProductID = models.IntegerField(primary_key=True)
    supplierID = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    productPrice = models.DecimalField(max_digits=10, decimal_places=2)
    productName = models.CharField(max_length=100)

    def __str__(self):
        return self.productName
    
class PRICE_CONTROL(models.Model):
    AMROfficerID = models.IntegerField(default=1)
    ProductID = models.ForeignKey(Product, on_delete=models.CASCADE, primary_key=True)
    Upper_Price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    Lower_Price = models.DecimalField(default=0, max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Upper Price is {self.Upper_Price} and Lower Price is {self.Lower_Price}'
    
class Farmer_Offered_Price(models.Model):
    # define the fields for your model
    farmerID = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    ProductID = models.ForeignKey(Product, on_delete=models.CASCADE)
    AMROfficerID = models.ForeignKey(PRICE_CONTROL, on_delete=models.CASCADE)
    offeredPrice = models.DecimalField(max_digits=10, decimal_places=2)

class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title
