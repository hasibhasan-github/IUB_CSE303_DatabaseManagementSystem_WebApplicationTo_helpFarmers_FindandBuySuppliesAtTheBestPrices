from django import forms 

class Testform(forms.Form):
    name = forms.CharField()