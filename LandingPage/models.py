from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    USER_TYPE_CHOICES = [
        ('supplier', 'Supplier'),
        ('farmer', 'Farmer'),
        ('ARDOFFICER', 'ARDOFFICER'),
    ]
    email = models.EmailField('Email address', unique=True)
    user_type = models.CharField('User Type', max_length=20, choices=USER_TYPE_CHOICES, blank=True, null=True)


