from django import forms
from .models import PRICE_CONTROL, Supplier, Product, Farmer_Offered_Price, Country, City


# class SetPriceForm(forms.Form):
#     Upper_Price = forms.IntegerField()
#     Lower_Price = forms.IntegerField()

# class SetPriceForm(forms.Form):
#     Upper_Price = forms.IntegerField(required=False)
#     Lower_Price = forms.IntegerField(required=False)


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

# class SetPriceForm(forms.ModelForm):
#     class Meta:
#         model = PRICE_CONTROL
#         # fields = ['Upper_Price', 'Lower_Price']
#         fields = "__all__"
        
#     def clean(self):
#         cleaned_data = super().clean()
#         Upper_Price = cleaned_data.get('Upper_Price')
#         Lower_Price = cleaned_data.get('Lower_Price')
#         AMROfficerID = cleaned_data.get('AMROfficerID')
#         ProductID = cleaned_data.get('ProductID')
        
#         if Upper_Price < Lower_Price:
#             raise forms.ValidationError('Upper Price should be greater than Lower Price')
#         return cleaned_data

class SetPriceForm(forms.ModelForm):
    class Meta:
        model = PRICE_CONTROL
        # fields = ['Upper_Price', 'Lower_Price']
        fields = "__all__"
        
    def clean(self):
        cleaned_data = super().clean()
        upper_price = cleaned_data.get('Upper_Price')
        lower_price = cleaned_data.get('Lower_Price')

        # Check if both upper_price and lower_price are not None and numeric before comparison
        if upper_price is not None and lower_price is not None:
            if isinstance(upper_price, (int, float)) and isinstance(lower_price, (int, float)):
                if upper_price < lower_price:
                    raise forms.ValidationError("Upper Price should be greater than Lower Price")

        return cleaned_data


# class SetPriceForm(forms.ModelForm):
#     class Meta:
#         model = PRICE_CONTROL
#         fields = ['Upper_Price', 'Lower_Price']

#     def clean(self):
#         cleaned_data = super().clean()

#         # Check if both prices are present and numeric
#         upper_price = cleaned_data.get('Upper_Price')
#         lower_price = cleaned_data.get('Lower_Price')
#         if not upper_price or not lower_price:
#             raise forms.ValidationError("Both Upper Price and Lower Price are required.")

#         # Check if values are numeric and Upper Price is greater than Lower Price
#         if not isinstance(upper_price, (int, float)) or not isinstance(lower_price, (int, float)):
#             raise forms.ValidationError("Please enter valid numbers for both prices.")
#         if upper_price < lower_price:
#             raise forms.ValidationError("Upper Price should be greater than Lower Price")

#         return cleaned_data


# class PriceForm(forms.Form):
#     Upper_Price = forms.DecimalField(label="Set Upper Price", widget=forms.TextInput(attrs={"class": "form-control"}), required=True)
#     Lower_Price = forms.DecimalField(label="Set Lower Price", widget=forms.TextInput(attrs={"class": "form-control"}), required=True)

# class PriceSettingForm(forms.Form):
#     Upper_Price = forms.DecimalField(label='UP', required=True, widget=forms.NumberInput(attrs={'id': 'id_Upper_Price'}))
#     Lower_Price = forms.DecimalField(label='LP', required=True, widget=forms.NumberInput(attrs={'id': 'id_Lower_Price'}))



SUPPLIER_CHOICES = [
    ('wholesale', 'Wholesale'),
    ('retail', 'Retail'),
    ('online', 'Online'),
]

class SupplierForm(forms.Form):
    supplier_type = forms.ChoiceField(label='Select Supplier Type', choices=SUPPLIER_CHOICES)
    # or, if you have a model field with choices
    # supplier_type = forms.ModelChoiceField(label='Select Supplier Type', queryset=Supplier.objects.all())

class FarmerOfferedPriceForm(forms.ModelForm):
    class Meta:
        model = Farmer_Offered_Price
        fields = ['farmerID', 'ProductID', 'AMROfficerID', 'offeredPrice']

# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ['ProductID', 'supplierID', 'productPrice', 'productName']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # Set the queryset for the 'supplier' field
#         self.fields['supplierID'].queryset = Supplier.objects.all()

class ProductForm(forms.Form):
    supplierID = forms.ChoiceField(choices=[], required=False, label='Select Supplier')
    ProductID = forms.ModelChoiceField(queryset=Product.objects.none(), required=False, label='Select Product')

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['supplierID'].choices = [(supplier.id, supplier.supplierType) for supplier in Supplier.objects.all()]

        # Initially, set the product choices to all products
        self.fields['ProductID'].queryset = Product.objects.all()

        # If a supplier is selected, update the product choices
        if 'supplierID' in self.data:
            supplierID = self.data.get('supplierID')
            self.fields['ProductID'].queryset = Product.objects.filter(supplierID=supplierID)
        elif self.is_bound and 'supplierID' not in self.data:
            # If the form is bound and supplierID is not in the data, reset the product choices
            self.fields['ProductID'].queryset = Product.objects.none()
            


# class LocationForm(forms.Form):
#     country = forms.ModelChoiceField(queryset=Country.objects.all(), required=False, label='Select Country')
#     city = forms.ModelChoiceField(queryset=City.objects.none(), required=False, label='Select City')
    
# class LocationForm(forms.Form):
#     country = forms.ModelChoiceField(queryset=Country.objects.all(),
#         widget=forms.Select(attrs={"hx-get": "load_cities/", "hx-target": "#id_city"}))
#     city = forms.ModelChoiceField(queryset=City.objects.none())

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         if "country" in self.data:
#             country_id = int(self.data.get("country"))
#             self.fields["city"].queryset = City.objects.filter(country_id=country_id)

class LocationForm(forms.Form):
    supplier = forms.ModelChoiceField(queryset=Supplier.objects.all(),
                                      widget=forms.Select(attrs={"hx-get": "load_products/", "hx-target": "#id_product"}))
    product = forms.ModelChoiceField(queryset=Product.objects.none())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set choices for the supplier field to display supplierType
        self.fields['supplier'].choices = [(supplier.supplierID, supplier.supplierType) for supplier in Supplier.objects.all()]

        if "supplier" in self.data:
            supplier_id = int(self.data.get("supplier"))
            self.fields["product"].queryset = Product.objects.filter(supplierID=supplier_id)

# forms.py

# class LocationForm(forms.Form):
#     supplier = forms.ModelChoiceField(
#         queryset=Supplier.objects.all(),
#         widget=forms.Select(attrs={"hx-get": "load_products/", "hx-target": "#id_product"})
#     )
#     product = forms.ModelChoiceField(queryset=Product.objects.none())
#     selected_supplier_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
#     selected_product_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         if "supplier" in self.data:
#             supplier_id = int(self.data.get("supplier"))
#             self.fields["product"].queryset = Product.objects.filter(supplierID=supplier_id)

#         if "product" in self.data:
#             product_id = int(self.data.get("product"))
#             self.fields["selected_product_id"].initial = product_id

#         if "selected_supplier_id" in self.data:
#             supplier_id = int(self.data.get("selected_supplier_id"))
#             self.fields["supplier"].queryset = Supplier.objects.filter(supplierID=supplier_id)

#     def clean(self):
#         cleaned_data = super().clean()
#         cleaned_data['selected_supplier_id'] = cleaned_data.get('supplier').supplierID
#         cleaned_data['selected_product_id'] = cleaned_data.get('product').ProductID
#         return cleaned_data

# class LocationForm(forms.Form):
#     supplier = forms.ModelChoiceField(queryset=Supplier.objects.none(),
#                                       widget=forms.Select(attrs={"hx-get": "load_products/", "hx-target": "#id_product"}))
#     product = forms.ModelChoiceField(queryset=Product.objects.none())

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         # Load initial choices for supplier
#         self.fields['supplier'].queryset = Supplier.objects.all()

#         # Load initial choices for product (if supplier is selected)
#         if 'supplier' in self.data:
#             supplier_id = int(self.data.get('supplier'))
#             self.fields['product'].queryset = Product.objects.filter(supplierID=supplier_id)


# class SetPriceForm(forms.ModelForm):
#     class Meta:
#         model = PRICE_CONTROL
#         fields = ['Upper_Price', 'Lower_Price']
#         fields = "__all__"


class SetPriceLocationForm(SetPriceForm, LocationForm, FarmerOfferedPriceForm, forms.ModelForm):
    # You can add additional fields or override the inherited ones here
    def clean(self):
        cleaned_data = super().clean()
        upper_price = cleaned_data.get('Upper_Price')
        lower_price = cleaned_data.get('Lower_Price')

        # Check if both upper_price and lower_price are not None and numeric before comparison
        if upper_price is not None and lower_price is not None:
            if isinstance(upper_price, (int, float)) and isinstance(lower_price, (int, float)):
                if upper_price < lower_price:
                    raise forms.ValidationError("Upper Price should be greater than Lower Price")

        return cleaned_data
    class Meta:
        model = Farmer_Offered_Price
        fields = ['farmerID', 'ProductID', 'AMROfficerID', 'offeredPrice']
        exclude = ["usern"]
        
    set_price_field = forms.CharField()




class BookSearchForm(forms.Form):
    genre = forms.CharField(label='Genre', max_length=20)
