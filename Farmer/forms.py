from django import forms


supplier = [
    ('suplier', ' Fertilizer Supplier'),
    ('suplier-2', ' Seed Supplier')

]

class userFrom(forms.Form):
    num1 = forms.CharField(label="value-1", required= True, widget= forms.TextInput(attrs={'class': "form-control mt-2 col-xs-5"}))
    num2 = forms.CharField(label="value-2", required= True, widget= forms.TextInput(attrs={'class': "form-control mt-2 col-xs-5"}))