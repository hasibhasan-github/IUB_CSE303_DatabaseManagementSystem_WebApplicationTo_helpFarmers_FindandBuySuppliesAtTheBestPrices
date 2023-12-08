from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.core.exceptions import ValidationError

class FixedSizeZipCharField(forms.CharField):
    default_validators = [MaxLengthValidator(limit_value=4), MinLengthValidator(limit_value=4)]

class FixedSizeContactCharField(forms.CharField):
    default_validators = [MaxLengthValidator(limit_value=11), MinLengthValidator(limit_value=11)]


class Suppliers(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    SUPPLIER_CHOICES = [
        ('fertilizer', 'Fertilizer Supplier'),
        ('equipementandmachineries', 'Equipment And Machineries Supplier'),
        ('seed', 'Seed Supplier'),
        ('coldstorage', 'Cold Storage Supplier'),
        ('cattleandfisheries', 'Cattle And Fisheries Supplier'),
    ]

    email = models.EmailField(unique=True)
    fname = models.CharField(max_length=10)
    lname = models.CharField(max_length=10)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    house = models.CharField(max_length=12)
    street = models.CharField(max_length=12)
    thana = models.CharField(max_length=12)
    zip = models.CharField(max_length=10)
    city = models.CharField(max_length=15)
    contactnumber = models.CharField(max_length=15)
    supplierType = models.CharField(max_length=50, choices=SUPPLIER_CHOICES)
    userType = models.CharField(max_length=20, default="Supplier")

    def __str__(self):
        return self.email

class CustomUserCreationForm(UserCreationForm):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    SUPPLIER_CHOICES = [
        ('fertilizer', 'Fertilizer Supplier'),
        ('equipementandmachineries', 'Equipement And Machineries Supplier'),
        ('seed', 'Seed Supplier'),
        ('coldstorage', 'Cold Storage Supplier'),
        ('cattleandfisheries', 'Cattle And Fisheries Supplier'),
    ]

    
    email = forms.EmailField()
    fname = forms.CharField(max_length=10)
    lname = forms.CharField(max_length=10)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    house = forms.CharField(max_length=12)
    street = forms.CharField(max_length=12)
    thana = forms.CharField(max_length=12)
    zip = FixedSizeZipCharField()
    city = forms.CharField(max_length=15)
    contactnumber = FixedSizeContactCharField()
    supplierType = forms.ChoiceField(choices=SUPPLIER_CHOICES)
    userType = forms.CharField(disabled=True, initial="Supplier")

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return email  # Email is unique
        raise ValidationError('This email is already in use.')
    
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        # Remove the username field
        if 'username' in self.fields:
            del self.fields['username']
            self.fields['username'] = self.fields['email']
            

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'fname', 'lname', 'gender', 'house', 'street', 'thana', 'zip', 'city', 'contactnumber', 'supplierType')


    # def clean_username(self):
    #     return self.cleaned_data['email']

