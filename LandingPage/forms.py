from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class LoginForm(forms.Form):
    # SUPPLIER_CHOICES = [
    #     ('fertilizer', 'Fertilizer Supplier'),
    #     ('equipementandmachineries', 'Equipment And Machineries Supplier'),
    #     ('seed', 'Seed Supplier'),
    #     ('coldstorage', 'Cold Storage Supplier'),
    #     ('cattleandfisheries', 'Cattle And Fisheries Supplier'),
    # ]

    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    # supplier_type = forms.ChoiceField(
    #     choices=SUPPLIER_CHOICES,
    #     widget=forms.Select(attrs={"class": "form-control"})
    # )

class SignUpForm(UserCreationForm):
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

    USER_TYPE_CHOICES = [
        ('supplier', 'Supplier'),
        ('farmer', 'Farmer'),
    ]

    email = forms.EmailField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    fname = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    lname = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"})
    )
    house = forms.CharField(
        max_length=12,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    street = forms.CharField(
        max_length=12,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    thana = forms.CharField(
        max_length=12,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    zip = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    city = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    contactnumber = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    supplierType = forms.ChoiceField(
        choices=SUPPLIER_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"})
    )
    userType = forms.CharField(
        max_length=20,
        #choices = USER_TYPE_CHOICES,
        #widget=forms.Select(attrs={"class": "form-control"}),
        widget=forms.HiddenInput(),
        initial="Supplier"
    )


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'user_type')

