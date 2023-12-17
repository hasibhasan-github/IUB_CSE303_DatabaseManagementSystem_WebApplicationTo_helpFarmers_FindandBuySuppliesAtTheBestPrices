from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, ListView, View, UpdateView, DeleteView
from my_app.models import PRICE_CONTROL, Supplier, Farmer, Product, Farmer_Offered_Price, Country, City
from my_app.forms import SetPriceForm, FarmerOfferedPriceForm, ProductForm, SupplierForm, LocationForm, SetPriceLocationForm
from django.http import HttpResponse, JsonResponse
# from chartit import DataPool, Chart

from django.db import connection

# Disable foreign key checks
cursor = connection.cursor()
cursor.execute('PRAGMA foreign_keys = OFF;')

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')

def table(request):
    return render(request, 'tables.html')

def notifications(request):
    return render(request, 'notifications.html')

def profile(request):
    return render(request, 'profile.html')

def sign_out(request):
    return render(request, 'sign_out.html')



class DashboardView (TemplateView):
    template_name = 'dashboard.html'




class DetailsView(ListView):
    template_name = 'details.html'
    context_object_name = 'details_list'

    def get_queryset(self):
        supplier_list = Supplier.objects.all()
        farmer_list = Farmer.objects.all()
        product_list = Product.objects.all()
        offered_price_list = Farmer_Offered_Price.objects.all()
        

        return list(zip(supplier_list, farmer_list, product_list, offered_price_list))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Supplier_List'], context['Farmer_List'], context['Product_List'], context['Offered_Price_List'] = zip(*self.get_queryset())
        return context
    



def Farmer_Offered_Price_Chart(request):
    productOfferPrices = Farmer_Offered_Price.objects.all()
    productOfferPrices_data = [{'farmerID': productOfferPrice.farmerID, 'ProductID': productOfferPrice.ProductID, 'AMROfficerID': productOfferPrice.AMROfficerID, 'offeredPrice': productOfferPrice.offeredPrice} for productOfferPrice in productOfferPrices]

    return render(request, 'your_template.html', {'product_data': productOfferPrices_data})


from .models import Book
from .forms import BookSearchForm

def book_search(request):
    # If the request is a POST request, process the form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request
        form = BookSearchForm(request.POST)
        # Check whether the form is valid
        if form.is_valid():
            # Get the genre from the form data
            genre = form.cleaned_data['genre']
            # Query the database for books with the given genre
            books = Book.objects.filter(genre=genre)
            # Render the template with the form and the books
            return render(request, 'details.html', {'form': form, 'books': books})
    # If the request is a GET request, create a blank form
    else:
        form = BookSearchForm()
        # Render the template with the form and no books
        return render(request, 'details.html', {'form': form})





class SetPriceListViewAndCreateView(View):
    template_name = 'tables.html'
    form_class = SetPriceLocationForm
    form_class_set_price = SetPriceForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        set_price_list = Farmer_Offered_Price.objects.all()
        return render(request, self.template_name, {'form': form, 'Set_Price_List': set_price_list})

    def post(self, request, *args, **kwargs):
        target_form = None
        selected_product = None
        amr_officer_id = 1
        print("Request POST:", request.POST)

        if request.POST.get('action') == 'product':
            target_form = self.form_class(request.POST)
            if target_form.is_valid():
                target_form.save()
                messages.success(request, 'Product saved successfully.')

        elif request.POST.get('action') == 'set_price':
            target_form = self.form_class_set_price(request.POST)
    
            if target_form.is_valid():
                product_name = target_form.cleaned_data.get('product') or request.POST.get('product')
                selected_product = get_object_or_404(Product, productName=product_name)
                try:
                    upper_price = target_form.cleaned_data.get('Upper_Price')
                    lower_price = target_form.cleaned_data.get('Lower_Price')
                    # Check if PRICE_CONTROL entry already exists for the product
                    price_control_instance, created = PRICE_CONTROL.objects.get_or_create(
                        ProductID=selected_product,
                        AMROfficerID=amr_officer_id,
                        defaults={'Upper_Price': upper_price, 'Lower_Price': lower_price}
                    )
                    if not created:
                        # Update existing entry if it already exists
                        price_control_instance.Upper_Price = upper_price
                        price_control_instance.Lower_Price = lower_price
                        price_control_instance.save()

                    messages.success(request, 'Prices set successfully.')
                except Exception as e:
                    messages.error(request, f'Error saving prices: {e}')

        if target_form and target_form.is_valid():
            product_name = target_form.cleaned_data.get('product') or request.POST.get('product')
            
            if isinstance(target_form, self.form_class):
                # Logic for the first form and saving product
                # ... additional logic ...
                pass
            elif isinstance(target_form, self.form_class_set_price):
                # Logic for the second form and setting price
                # ... existing code ...
                print("Product Name:", product_name)

            return redirect('my_app:Set_Price_List')

        else:
            product = kwargs.get('selected_product')
            
            if target_form:
                product_name = target_form.cleaned_data.get('product') or request.POST.get('product')
                product_id = product_name.ProductID
                selected_product = get_object_or_404(Product, productName=product_name)
                farmer_offered_price_exists = Farmer_Offered_Price.objects.filter(ProductID=selected_product).exists()
                offered_price_list = Farmer_Offered_Price.objects.filter(ProductID=selected_product)
                form_set_price = self.form_class_set_price()
                set_price_list = offered_price_list
    
                return render(request, self.template_name, {
                    'form': self.form_class,
                    'form_set_price': form_set_price,
                    'selected_product': selected_product,
                    'Offered_Price_List': offered_price_list,
                    'Set_Price_List': set_price_list,
                })

            messages.error(request, "Selected product is missing.")
            return redirect('my_app:Set_Price_List')


    
def load_products(request):
    supplier_id = request.GET.get("supplier")
    products = Product.objects.filter(supplierID=supplier_id)
    return render(request, "products_options.html", {"products": products})
