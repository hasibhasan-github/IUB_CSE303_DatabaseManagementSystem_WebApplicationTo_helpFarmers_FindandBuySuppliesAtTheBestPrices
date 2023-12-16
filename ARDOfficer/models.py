from django.db import models

# Create your models here.
class ardTable(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, blank=True)
    house = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    thana = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)
    city = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=15)  # Assuming a simple string for now
    officer_type = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.fname} {self.lname} ({self.email})"