from django import forms
from .models import Set_Price

# class SetPriceForm(forms.Form):
#     Upper_Price = forms.IntegerField()
#     Lower_Price = forms.IntegerField()

# class SetPriceForm(forms.Form):
#     Upper_Price = forms.IntegerField()
#     Lower_Price = forms.IntegerField()
    
#     def clean(self):
#         cleaned_data = super().clean()
#         Upper_Price = cleaned_data.get('Upper_Price')
#         Lower_Price = cleaned_data.get('Lower_Price')
        
#         if Upper_Price < Lower_Price:
#             raise forms.ValidationError('Upper Price should be greater than Lower Price')
#         return cleaned_data

class SetPriceForm(forms.ModelForm):
    class Meta:
        model = Set_Price
        fields = ['Upper_Price', 'Lower_Price']
        fields = "__all__"
        
    def clean(self):
        cleaned_data = super().clean()
        Upper_Price = cleaned_data.get('Upper_Price')
        Lower_Price = cleaned_data.get('Lower_Price')
        
        if Upper_Price < Lower_Price:
            raise forms.ValidationError('Upper Price should be greater than Lower Price')
        return cleaned_data

# class PriceForm(forms.Form):
#     Upper_Price = forms.DecimalField(label="Set Upper Price", widget=forms.TextInput(attrs={"class": "form-control"}), required=True)
#     Lower_Price = forms.DecimalField(label="Set Lower Price", widget=forms.TextInput(attrs={"class": "form-control"}), required=True)

# class PriceSettingForm(forms.Form):
#     Upper_Price = forms.DecimalField(label='UP', required=True, widget=forms.NumberInput(attrs={'id': 'id_Upper_Price'}))
#     Lower_Price = forms.DecimalField(label='LP', required=True, widget=forms.NumberInput(attrs={'id': 'id_Lower_Price'}))
