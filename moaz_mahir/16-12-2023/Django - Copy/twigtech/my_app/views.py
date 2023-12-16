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

# class SetPriceListView (ListView):
#     template_name = 'tables.html'
#     model = Set_Price

# class SetPriceListView (ListView):
#     template_name = 'tables.html'
#     model = Set_Price
#     context_object_name = 'Set_Price_List'
#     ordering = ['-Upper_Price']
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['Set_Price_List'] = Set_Price.objects.all()
#         return context

    
# class SetPriceFormView (FormView):
#     template_name = 'my_app/set_price.html'
#     form_class = SetPriceForm
#     success_url = '/set_price_list/'

#     def form_valid(self, form):
#         print(form.cleaned_data)
#         # form.save()
#         return super().form_valid(form)
    
# class SetPriceCreateView (CreateView):
#     template_name = 'tables.html'
#     form_class = SetPriceForm
#     model = Set_Price
#     # fields = ['Upper_Price', 'Lower_Price']
#     # fields = "__all__"
#     success_url = reverse_lazy('my_app:Set_Price_List')
    
#     def get_success_url(self):
#         return reverse('my_app:Set_Price_List')
    
#     def form_valid(self, form):
#         print(form.cleaned_data)
#         return super().form_valid(form)
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['Set_Price_List'] = Set_Price.objects.all()
#         return context

'''
class SetPriceListView(ListView):
    template_name = 'tables.html'
    model = Set_Price
    context_object_name = 'set_prices'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SetPriceForm()
        return context

    def post(self, request, *args, **kwargs):
        form = SetPriceForm(request.POST)
        if form.is_valid():
            form.save()
        return self.get(request, *args, **kwargs)

class SetPriceCreateView(CreateView):
    template_name = 'tables.html'
    form_class = SetPriceForm
    model = Set_Price
    success_url = reverse_lazy('my_app:Set_Price_List')

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['set_prices'] = Set_Price.objects.all()
        return context
'''

# class SetPriceView(TemplateView):
#     template_name = 'tables.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = SetPriceForm()
#         context['Set_Price_List'] = Set_Price.objects.all()
#         return context

#     def post(self, request, *args, **kwargs):
#         form = SetPriceForm(request.POST)
#         if form.is_valid():
#             # Process the form and save data
#             form.save()
#             # Redirect to the same page to display the updated data
#             return redirect(reverse_lazy('my_app:Set_Price_List'))
#         else:
#             # If the form is not valid, re-render the page with the form and existing data
#             context = self.get_context_data(form=form)
#             return self.render_to_response(context)
        
# class SetPriceListView(ListView):
#     template_name = 'tables.html'
#     model = Set_Price
#     context_object_name = 'Set_Price_List'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = SetPriceForm()
#         return context

#     def post(self, request, *args, **kwargs):
#         form = SetPriceForm(request.POST)
#         if form.is_valid():
#             # Process the form and save data
#             form.save()
#             # Reload the page to display the updated data
#             return redirect(reverse_lazy('my_app:Set_Price_List'))
#         else:
#             # If the form is not valid, re-render the page with the form and existing data
#             context = self.get_context_data(form=form)
#             return self.render_to_response(context)

# class SetPriceCreateListView(ListView, CreateView):
#     template_name = 'tables.html'
#     form_class = SetPriceForm
#     model = Set_Price
#     success_url = reverse_lazy('my_app:Set_Price_List')

#     def get_success_url(self):
#         return reverse('my_app:Set_Price_List')

#     def form_valid(self, form):
#         print(form.cleaned_data)
#         return super().form_valid(form)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['Set_Price_List'] = Set_Price.objects.all()
#         return context


# class SetPriceListViewAndCreateView(View):
#     template_name = 'tables.html'
#     form_class = SetPriceForm

#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         set_price_list = PRICE_CONTROL.objects.all()
#         return render(request, self.template_name, {'form': form, 'Set_Price_List': set_price_list})

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('my_app:Set_Price_List')
#         set_price_list = PRICE_CONTROL.objects.all()
#         return render(request, self.template_name, {'form': form, 'Set_Price_List': set_price_list})

'''
#works for diffrent
class SetPriceListViewAndCreateView(View):
    template_name = 'tables.html'
    form_class = SetPriceForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        set_price_list = PRICE_CONTROL.objects.all()
        return render(request, self.template_name, {'form': form, 'Set_Price_List': set_price_list})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_app:Set_Price_List')
        set_price_list = PRICE_CONTROL.objects.all()
        return render(request, self.template_name, {'form': form, 'Set_Price_List': set_price_list})


def index(request):
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            # Process the valid form data here
            print(form.cleaned_data["supplier"])
            print(form.cleaned_data["product"])
        else:
            print(form.errors)
    else:
        # For GET requests, initialize the form with initial data if needed
        form = LocationForm()

    return render(request, 'tables.html', {"form": form})


def load_products(request):
    supplier_id = request.GET.get("supplier")
    products = Product.objects.filter(supplierID=supplier_id)
    return render(request, "products_options.html", {"products": products})

'''

# class SetPriceListViewAndCreateView(View):
#     template_name = 'tables.html'
#     set_price_form_class = SetPriceForm
#     location_form_class = LocationForm

#     def get(self, request, *args, **kwargs):
#         set_price_form = self.set_price_form_class()
#         location_form = self.location_form_class()
#         set_price_list = PRICE_CONTROL.objects.all()
#         products = Product.objects.all()
#         return render(request, self.template_name, {
#             'set_price_form': set_price_form,
#             'location_form': location_form,
#             'Set_Price_List': set_price_list,
#             'products': products,
#         })

#     def post(self, request, *args, **kwargs):
#         set_price_form = self.set_price_form_class(request.POST)
#         location_form = self.location_form_class(request.POST)

#         if set_price_form.is_valid():
#             set_price_form.save()
#             return redirect('my_app:set_price_list')  # Assuming 'set_price_list' is the correct URL name

#         set_price_list = PRICE_CONTROL.objects.all()
#         products = Product.objects.all()

#         return render(request, self.template_name, {
#             'set_price_form': set_price_form,
#             'location_form': location_form,
#             'Set_Price_List': set_price_list,
#             'products': products,
#         })

# def load_products(request):
#     supplier_id = request.GET.get("supplier")
#     products = Product.objects.filter(supplierID=supplier_id)
#     return render(request, "products_options.html", {"products": products})
'''
class SetPriceListViewAndCreateView(View):
    template_name = 'tables.html'
    form_class = SetPriceForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        set_price_list = PRICE_CONTROL.objects.all()
        location_form = LocationForm()  # Initialize LocationForm for supplier and product selection
        return render(request, self.template_name, {'form': form, 'Set_Price_List': set_price_list, 'location_form': location_form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_app:Set_Price_List')
        set_price_list = PRICE_CONTROL.objects.all()
        location_form = LocationForm(request.POST)  # Populate LocationForm with submitted data
        return render(request, self.template_name, {'form': form, 'Set_Price_List': set_price_list, 'location_form': location_form})

'''





# class SetPriceListViewAndCreateView(View):
#     template_name = 'tables.html'
#     form_class_supplier = LocationForm
#     form_class_price = SetPriceForm

#     def get(self, request, *args, **kwargs):
#         form_supplier = self.form_class_supplier()
#         form_price = self.form_class_price()

#         set_price_list = PRICE_CONTROL.objects.all()

#         return render(request, self.template_name, {
#             'form_supplier': form_supplier,
#             'form_price': form_price,
#             'Set_Price_List': set_price_list
#         })

#     def post(self, request, *args, **kwargs):
#         form_supplier = self.form_class_supplier(request.POST)
#         form_price = self.form_class_price(request.POST)

#         if form_supplier.is_valid() and form_price.is_valid():
#             # Process the valid form data here
#             supplier_id = form_supplier.cleaned_data['supplier']
#             product_id = form_supplier.cleaned_data['product']

#             # Perform actions with supplier_id, product_id, and form_price.cleaned_data

#             return redirect('my_app:Set_Price_List')  # Redirect to the desired URL

#         set_price_list = PRICE_CONTROL.objects.all()

#         return render(request, self.template_name, {
#             'form_supplier': form_supplier,
#             'form_price': form_price,
#             'Set_Price_List': set_price_list
#         })
'''
class SetPriceListViewAndCreateView(View):
    template_name = 'tables.html'
    # Change the form_class attribute to SetPriceLocationForm
    form_class = SetPriceLocationForm

    # def get(self, request, *args, **kwargs):
    #     form = self.form_class()
    #     set_price_list = PRICE_CONTROL.objects.all()
    #     return render(request, self.template_name, {'form': form, 'Set_Price_List': set_price_list})
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        set_price_list = Farmer_Offered_Price.objects.all()
        return render(request, self.template_name, {'form': form, 'Set_Price_List': set_price_list})

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('my_app:Set_Price_List')
    #     set_price_list = PRICE_CONTROL.objects.all()
    #     return render(request, self.template_name, {'form': form, 'Set_Price_List': set_price_list})
    
    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         supplier_id = form.cleaned_data['supplier']
    #         product_id = form.cleaned_data['product']
    #         # Get the supplier and product objects from the database, or raise a 404 error
    #         supplier = get_object_or_404(Farmer, id=supplier_id)
    #         product = get_object_or_404(Product, id=product_id)
    #         # Get the offered price list for the selected supplier and product
    #         offered_price_list = Farmer_Offered_Price.objects.filter(ProductID=product)
    #         # Save the form instance with the request user as the usern field
    #         form.instance.usern = request.user
    #         form.save()
    #         # Render the template with the form and the offered price list
    #         return render(request, self.template_name, {'form': form, 'Offered_Price_List': offered_price_list})
    #     # If the form is invalid, render the template with the form errors
    #     return render(request, self.template_name, {'form': form})
    
    # def post(self, request, *args, **kwargs):
    #         form = self.form_class(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             return redirect('my_app:Set_Price_List')
    #         product_id = form.cleaned_data['product']
    #         product = get_object_or_404(Product, productName=product_id)
    #         offered_price_list = Farmer_Offered_Price.objects.filter(ProductID=product)
    #         # offered_price_list = Farmer_Offered_Price.objects.all()
    #         return render(request, self.template_name, {'form': form, 'Offered_Price_List': offered_price_list})


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_app:Set_Price_List')

        # Retrieve the selected product using productName
        product_name = form.cleaned_data['product']
        product = get_object_or_404(Product, productName=product_name)
        
        print("producthhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh ID:", product.ProductID)
        

        # Filter offered prices based on the selected product
        offered_price_list = Farmer_Offered_Price.objects.filter(ProductID=product.ProductID)

        set_price_list = Farmer_Offered_Price.objects.all()
        return render(request, self.template_name, {'form': form, 'Offered_Price_List': offered_price_list, 'Set_Price_List': set_price_list})

    
# class SetPriceListViewAndCreateView(View):
#     template_name = 'tables.html'
#     form_class = SetPriceLocationForm

#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         return render(request, self.template_name, {'form': form})

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             supplier_id = form.cleaned_data['supplier']
#             product_id = form.cleaned_data['product']
#             offered_price_list = Farmer_Offered_Price.objects.filter(ProductID=product_id, supplierID=supplier_id)
#             return render(request, self.template_name, {'form': form, 'Offered_Price_List': offered_price_list})
#         return render(request, self.template_name, {'form': form})

# class SetPriceListViewAndCreateView(View):
#     template_name = 'tables.html'
#     form_class = SetPriceLocationForm

#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         return render(request, self.template_name, {'form': form})

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             supplier_id = form.cleaned_data['supplier']
#             product_id = form.cleaned_data['product']
#             # Get the supplier and product objects from the database, or raise a 404 error
#             supplier = get_object_or_404(Farmer, id=supplier_id)
#             product = get_object_or_404(Product, id=product_id)
#             # Get the offered price list for the selected supplier and product
#             offered_price_list = Farmer_Offered_Price.objects.filter(farmer=supplier, product=product)
#             # Save the form instance with the request user as the usern field
#             form.instance.usern = request.user
#             form.save()
#             # Render the template with the form and the offered price list
#             return render(request, self.template_name, {'form': form, 'offered_price_list': offered_price_list})
#         # If the form is invalid, render the template with the form errors
#         return render(request, self.template_name, {'form': form})


def load_products(request):
    supplier_id = request.GET.get("supplier")
    products = Product.objects.filter(supplierID=supplier_id)
    return render(request, "products_options.html", {"products": products})

'''

# class SetPriceListViewAndCreateView(View):
#     template_name = 'tables.html'
#     form_class = SetPriceForm

#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         set_price_list = PRICE_CONTROL.objects.all()

#         try:
#             set_price_list = [item for item in set_price_list if isinstance(item, (int, float))]
#             print("Set_Price_List:", set_price_list)
#             return render(request, self.template_name, {'form': form, 'Set_Price_List': set_price_list})
#         except Exception as e:
#             print("Error in rendering:", e)
#             # Handle the error gracefully, for example, by providing a default value
#             set_price_list = []  # Provide an empty list or any default value
#             return render(request, self.template_name, {'form': form, 'Set_Price_List': set_price_list})


#         # return render(request, self.template_name, {'form': form, 'Set_Price_List': set_price_list})

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('my_app:Set_Price_List')
#         set_price_list = PRICE_CONTROL.objects.all()
        
#         try:
#             set_price_list = [item for item in set_price_list if isinstance(item, (int, float))]
#             print("Set_Price_List:", set_price_list)
#             return render(request, self.template_name, {'form': form, 'Set_Price_List': set_price_list})
#         except Exception as e:
#             print("Error in rendering:", e)
#             # Handle the error gracefully, for example, by providing a default value
#             set_price_list = []  # Provide an empty list or any default value
#             return render(request, self.template_name, {'form': form, 'Set_Price_List': set_price_list})
        
#         # return render(request, self.template_name, {'form': form, 'Set_Price_List': set_price_list})


# class DetailsView (ListView):
#     template_name = 'details.html'
#     model = Supplier
# class DetailsView (ListView):
#     template_name = 'details.html'
#     model = Supplier
#     context_object_name = 'Supplier_List'
#     # ordering = ['-productPrice']
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['Supplier_List'] = Supplier.objects.all()
#         return context
# class DetailsView(ListView):
#     template_name = 'details.html'
#     context_object_name = 'details_list'

#     def get_queryset(self):
#         supplier_list = Supplier.objects.all()
#         product_list = Product.objects.all()
#         offered_price_list = Farmer_Offered_Price.objects.all()

#         return list(zip(supplier_list, product_list, offered_price_list))

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['Supplier_List'], context['Product_List'], context['Offered_Price_List'] = zip(*self.get_queryset())
#         return context
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
    


# def your_view(request):
#     form = ProductForm(request.GET)
#     return render(request, 'details.html', {'form': form})


# class DetailsView(ListView):
#     template_name = 'details.html'
#     context_object_name = 'details_list'

#     def get_queryset(self):
#         supplier_list = Supplier.objects.all()
#         product_list = Product.objects.all()
#         offered_price_list = Farmer_Offered_Price.objects.all()
#         return list(zip(supplier_list, product_list, offered_price_list))
        

#         # # Ensure all lists have the same length before zipping
#         # if len(supplier_list) == len(product_list) == len(offered_price_list):
#         #     return list(zip(supplier_list, product_list, offered_price_list))
#         # else:
#         #     # Handle the case when lists have different lengths
#         #     # You can log an error or raise an exception based on your requirements
#         #     return []

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         queryset = self.get_queryset()

#         if queryset:
#             context['Supplier_List'], context['Product_List'], context['Offered_Price_List'] = zip(*queryset)
#         else:
#             # Set default values if the queryset is empty
#             context['Supplier_List'] = []
#             context['Product_List'] = []
#             context['Offered_Price_List'] = []

#         return context

# class DetailsView(View):
#     template_name = 'details.html'

#     def get(self, request, *args, **kwargs):
#         set_price_form = SetPriceForm()
#         offered_price_form = FarmerOfferedPriceForm()
#         product_form = ProductForm()

#         suppliers = Supplier.objects.all()
#         products = Product.objects.all()

#         return render(request, self.template_name, {
#             'set_price_form': set_price_form,
#             'offered_price_form': offered_price_form,
#             'product_form': product_form,
#             'suppliers': suppliers,
#             'products': products,
#         })

#     def post(self, request, *args, **kwargs):
#         set_price_form = SetPriceForm(request.POST)
#         offered_price_form = FarmerOfferedPriceForm(request.POST)
#         product_form = ProductForm(request.POST)

#         # if set_price_form.is_valid() and offered_price_form.is_valid() and product_form.is_valid():
#             # Process your forms and save data here

#         # Retrieve suppliers and products again to render the form with updated options
#         suppliers = Supplier.objects.all()
#         products = Product.objects.all()

#         return render(request, self.template_name, {
#             'set_price_form': set_price_form,
#             'offered_price_form': offered_price_form,
#             'product_form': product_form,
#             'suppliers': suppliers,
#             'products': products,
#         })

# class DetailsView(View):
#     template_name = 'details.html'

#     def get(self, request, *args, **kwargs):
#         supplier_id = request.GET.get('supplierID')
#         supplier_list = Supplier.objects.all()
#         product_list = Product.objects.filter(supplier_id=supplier_id) if supplier_id else Product.objects.all()
#         offered_price_list = Farmer_Offered_Price.objects.all()

#         context = {
#             'Supplier_List': supplier_list,
#             'Product_List': product_list,
#             'Offered_Price_List': offered_price_list,
#         }

#         return render(request, self.template_name, context)

# class DetailsView(View):
#     template_name = 'details.html'

#     def get(self, request, *args, **kwargs):
#         suppliers = Supplier.objects.all()
#         products = Product.objects.all()

#         selected_supplier_id = request.GET.get('supplierID')

#         if selected_supplier_id:
#             products = Product.objects.filter(supplier_id=selected_supplier_id)

#         return render(request, self.template_name, {'suppliers': suppliers, 'products': products})


# class DetailsView(View):
#     template_name = 'details.html'

#     def get(self, request, *args, **kwargs):
#         suppliers = Supplier.objects.all()
#         products = Product.objects.none()

#         selected_supplier_id = request.GET.get('supplierID')

#         if selected_supplier_id:
#             products = Product.objects.filter(supplierID=selected_supplier_id)

#         form = ProductForm(initial={'supplierID': selected_supplier_id})
#         return render(request, self.template_name, {'suppliers': suppliers, 'products': products, 'form': form})




# def index(request):
#     if request.method == "POST":
#         form = LocationForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data["country"])
#             print(form.cleaned_data["city"])
#         else:
#             print(form.errors)
#     else:
#         form = LocationForm()
#     return render(request, 'details.html', {"form": form})

# def load_cities(request):
#     country_id = request.GET.get("country")
#     cities = City.objects.filter(country_id=country_id)
#     return render(request, "city_options.html", {"cities": cities})


# def index(request):
#     if request.method == "POST":
#         form = LocationForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data["supplier"])
#             print(form.cleaned_data["product"])
#         else:
#             print(form.errors)
#     else:
#         form = LocationForm()
#     return render(request, 'details.html', {"form": form})

# def load_products(request):
#     supplier_id = request.GET.get("supplier")
#     products = Product.objects.filter(supplierID=supplier_id)
#     return render(request, "products_options.html", {"products": products})

# def index(request):
#     if request.method == "POST":
#         form = LocationForm(request.POST)
#         if form.is_valid():
#             # Process the valid form data here
#             print(form.cleaned_data["supplier"])
#             print(form.cleaned_data["product"])
#         else:
#             print(form.errors)
#     else:
#         # For GET requests, initialize the form with initial data if needed
#         form = LocationForm()

#     return render(request, 'tables.html', {"form": form})


# def load_products(request):
#     supplier_id = request.GET.get("supplier")
#     products = Product.objects.filter(supplierID=supplier_id)
#     return render(request, "products_options.html", {"products": products})


# def product_form(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # do something with the saved data
#     else:
#         form = ProductForm()
#     return render(request, 'product_form.html', {'form': form})

# def load_products(request):
#     # get the selected supplier id from the request
#     supplier_id = request.GET.get('supplierID')
#     # get the products that belong to the selected supplier
#     products = Product.objects.filter(supplierID=supplier_id).order_by('productName')
#     # return a JSON response with the product choices
#     return JsonResponse({
#         'products': [{'id': product.supplierID, 'name': product.productName} for product in products]
#     })


# def product_prices_chart(request):
#     # Assuming you have a Product model with productName and productPrice fields
#     products = Product.objects.all()

#     # Create a DataPool
#     product_data = DataPool(series=[{
#         'options': {
#             'source': products
#         },
#         'terms': [
#             'productName',
#             'productPrice'
#         ]
#     }])

#     # Create a PieChart
#     cht = Chart(
#         datasource=product_data,
#         series_options=[{
#             'options': {
#                 'type': 'pie',
#                 'center': ['50%', '50%'],
#                 'size': '60%',
#                 'showInLegend': True
#             },
#             'terms': {
#                 'productName': [
#                     'productPrice'
#                 ]
#             }
#         }],
#         chart_options={
#             'title': {
#                 'text': 'Product Offered Prices'
#             }
#         }
#     )

#     return render(request, 'your_template.html', {'cht': cht})



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


#==============================================================================
#                                       worked
#==============================================================================

# class SetPriceListViewAndCreateView(View):
#     template_name = 'tables.html'
#     # Change the form_class attribute to SetPriceLocationForm
#     form_class = SetPriceLocationForm

#     # def get(self, request, *args, **kwargs):
#     #     form = self.form_class()
#     #     set_price_list = PRICE_CONTROL.objects.all()
#     #     return render(request, self.template_name, {'form': form, 'Set_Price_List': set_price_list})
    
#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         set_price_list = Farmer_Offered_Price.objects.all()
#         return render(request, self.template_name, {'form': form, 'Set_Price_List': set_price_list})

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('my_app:Set_Price_List')

#         # Retrieve the selected product using productName
#         product_name = form.cleaned_data['product']
#         product = get_object_or_404(Product, productName=product_name)
        
#         # Filter offered prices based on the selected product
#         offered_price_list = Farmer_Offered_Price.objects.filter(ProductID=product.ProductID)

#         set_price_list = Farmer_Offered_Price.objects.all()
#         return render(request, self.template_name, {'form': form, 'selected_product': product, 'Offered_Price_List': offered_price_list, 'Set_Price_List': set_price_list})
# def load_products(request):
#     supplier_id = request.GET.get("supplier")
#     products = Product.objects.filter(supplierID=supplier_id)
#     return render(request, "products_options.html", {"products": products})

#==============================================================================#==============================================================================
#==============================================================================#==============================================================================


# class SetPriceListViewAndCreateView(View):
#     template_name = 'tables.html'
#     form_class = SetPriceLocationForm

#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         set_price_list = Farmer_Offered_Price.objects.all()
#         return render(request, self.template_name, {'form': form, 'Set_Price_List': set_price_list})

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)

#         if form.is_valid():
#             # Save the offered price
#             form.save()

#             # Retrieve the selected product using productName
#             product_name = form.cleaned_data['product']
#             product = get_object_or_404(Product, productName=product_name)

#             # Filter offered prices based on the selected product
#             offered_price_list = Farmer_Offered_Price.objects.filter(ProductID=product.ProductID)

#             # Filter set prices based on the selected product
#             set_price_list = PRICE_CONTROL.objects.filter(ProductID=product)

#             # Pass the selected product, offered prices, and set prices to the template
#             return render(request, self.template_name, {'form': form, 'selected_product': product, 'Offered_Price_List': offered_price_list, 'Set_Price_List': set_price_list})

#         # If form is not valid, render the template with the form
#         return render(request, self.template_name, {'form': form})



# def load_products(request):
#     supplier_id = request.GET.get("supplier")
#     products = Product.objects.filter(supplierID=supplier_id)
#     return render(request, "products_options.html", {"products": products})

########
# class SetPriceListViewAndCreateView(View):
#     template_name = 'tables.html'
#     form_class = SetPriceForm

#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         set_price_list = Farmer_Offered_Price.objects.all()
#         return render(request, self.template_name, {'form': form, 'Set_Price_List': set_price_list})

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('my_app:Set_Price_List')
#         set_price_list = Farmer_Offered_Price.objects.all()
#         return render(request, self.template_name, {'form': form, 'Set_Price_List': set_price_list})
###########
'''
# class SetPriceListViewAndCreateView(View):
#     template_name = 'tables.html'
#     # Change the form_class attribute to SetPriceLocationForm
#     form_class = SetPriceLocationForm
#     form_class_set_price = SetPriceForm

#     # def get(self, request, *args, **kwargs):
#     #     form = self.form_class()
#     #     set_price_list = PRICE_CONTROL.objects.all()
#     #     return render(request, self.template_name, {'form': form, 'Set_Price_List': set_price_list})
    
#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         form_set_price = self.form_class_set_price()
#         set_price_list = Farmer_Offered_Price.objects.all()
#         return render(request, self.template_name, {'form': form, 'form_set_price': form_set_price, 'Set_Price_List': set_price_list})

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             form.save()
#             # return redirect('my_app:Set_Price_List')

#         product_name = form.cleaned_data.get('product', None)
#         # print("product_name:", product_name)
#         if product_name:
#             product = get_object_or_404(Product, productName=product_name)
#             print("product:", product)
#             # Check if there is an existing Farmer_Offered_Price entry for the selected product
#             farmer_offered_price_exists = Farmer_Offered_Price.objects.filter(ProductID=product).exists()
#             print("farmer_offered_price_exists:", farmer_offered_price_exists)
            
#             if farmer_offered_price_exists:
#                 # Filter offered prices based on the selected product
#                 offered_price_list = Farmer_Offered_Price.objects.filter(ProductID=product.ProductID)
#                 print("product.ProductID:", product.ProductID)
#                 # Check if there is an existing PRICE_CONTROL entry for the selected product
#                 price_control_exists = PRICE_CONTROL.objects.filter(ProductID=product).exists()
#                 print("price_control_exists:", price_control_exists)
#                 if price_control_exists:
#                     # message = messages.error(request, f"Prices for {product.productName} are already set.")
#                     print("price_control_exists:", f"Prices for {product.productName} are already set.")
#                 else:
#                     # If not, create a new PRICE_CONTROL entry and set the prices
#                     form_set_price = self.form_class_set_price(request.POST)
#                     print("product.ProductID:", product.ProductID)
#                     print("product_name:", product_name)
#                     # price_control = PRICE_CONTROL.objects.create(ProductID=product)
#                     # print("price_control:", price_control)
#                     # price_control.Upper_Price = self.form_class_set_price(request.POST)
#                     # price_control.Lower_Price = self.form_class_set_price(request.POST)
                    
#                     if form_set_price.is_valid():
#                         form_set_price.save()
#                         # price_control.save()
#                         print("product.ProductID:", product.ProductID)
#                         print("product_name:", product_name)
#                         return redirect('my_app:Set_Price_List')
#                     else:
#                         # messages.error(request, f"Prices for {product.productName} are already set.")
#                         print("price_control_exists FAILED:", f"Prices for {product.productName} are not set.")
#             else:
#                 # message = messages.error(request, f"Farmer offered Price for {product.productName} are not exists.")
#                 print("farmer_offered_price_exists:", f"Farmer offered Price for {product.productName} are not exists.")
#                 return redirect('my_app:Set_Price_List')


                

#             set_price_list = Farmer_Offered_Price.objects.all()
#             return render(request, self.template_name, {'form': form, 'selected_product': product, 'Offered_Price_List': offered_price_list, 'Set_Price_List': set_price_list})

#         return render(request, self.template_name, {'form': form})
'''

# class SetPriceListViewAndCreateView(View):
#     template_name = 'tables.html'
#     # Change the form_class attribute to SetPriceLocationForm
#     form_class = SetPriceLocationForm
#     form_class_set_price = SetPriceForm

    # def get(self, request, *args, **kwargs):
    #     form = self.form_class()
    #     set_price_list = PRICE_CONTROL.objects.all()
    #     return render(request, self.template_name, {'form': form, 'Set_Price_List': set_price_list})
    
    # def get(self, request, *args, **kwargs):
    #     form = self.form_class()
    #     form_set_price = self.form_class_set_price()
    #     set_price_list = Farmer_Offered_Price.objects.all()
    #     return render(request, self.template_name, {'form': form, 'form_set_price': form_set_price, 'Set_Price_List': set_price_list})

    # def post(self, request, *args, **kwargs):
    #     form1 = self.form_class()
    #     form2 = self.form_class_set_price()

    #     if request.method == "POST":
    #         # if 'form1_submit' in request.POST:
    #             form1 = self.form_class(request.POST)
    #             if form1.is_valid():
    #                 product_name = form1.cleaned_data.get('product', None)
    #                 print("product_name:", product_name)
    #                 form1.save()
    #                 return redirect('my_app:Set_Price_List')
    #                 name = form1.cleaned_data['name']
    #                 email = form1.cleaned_data['email']
    #                 data = FormModel1.objects.create(name=name, email=email)
    #                 data.save()
    #             else:
    #                 # Handle form1 errors
    #                 return render(request, self.template_name, {'form1': form1, 'form2': form2})
    #     if request.method == "POST":
    #         # if 'form2_submit' in request.POST:
    #             form2 = self.form_class_set_price(request.POST)
    #             if form2.is_valid():
    #                 name = form2.cleaned_data['name']
    #                 email = form2.cleaned_data['email']
    #                 # data = FormModel1.objects.create(name=name, email=email)
    #                 # data.save()
    #             else:
    #                 # Handle form2 errors
    #                 return render(request, self.template_name, {'form1': form1, 'form2': form2})

    #     return render(request, self.template_name, {'form1': form1, 'form2': form2})
    
    # def post(self, request, *args, **kwargs):
    #     if request.method == 'POST':
    #         form = self.form_class(request.POST)
    #         print("Request POST:", request.POST)
    #         if form.is_valid():
    #             form.save()
    #             # return redirect('my_app:Set_Price_List')

    #         product_name = form.cleaned_data.get('product', None)
    #         # print("product_name:", product_name)
    #         if product_name:
    #             product = get_object_or_404(Product, productName=product_name)
    #             print("product:", product)
    #             # Check if there is an existing Farmer_Offered_Price entry for the selected product
    #             farmer_offered_price_exists = Farmer_Offered_Price.objects.filter(ProductID=product).exists()
    #             print("farmer_offered_price_exists:", farmer_offered_price_exists)

    #             if farmer_offered_price_exists:
    #                 # Filter offered prices based on the selected product
    #                 offered_price_list = Farmer_Offered_Price.objects.filter(ProductID=product.ProductID)
    #                 print("product.ProductID:", product.ProductID)
    #                 # Check if there is an existing PRICE_CONTROL entry for the selected product
    #                 price_control_exists = PRICE_CONTROL.objects.filter(ProductID=product).exists()
    #                 print("price_control_exists:", price_control_exists)
    #                 if price_control_exists:
    #                     # message = messages.error(request, f"Prices for {product.productName} are already set.")
    #                     print("price_control_exists:", f"Prices for {product.productName} are already set.")
    #                     return redirect('my_app:Set_Price_List')
    #                 else:
    #                     # If not, create a new PRICE_CONTROL entry and set the prices
    #                     price_control = PRICE_CONTROL.objects.create(ProductID=product)
                        
    #                     if request.method == 'POST':
    #                         form_set_price = self.form_class_set_price(request.POST)
    #                         print("Request POST:", request.POST)
    #                         print("product.ProductID:", product.ProductID)
    #                         print("product_name:", product_name)

    #                         if form_set_price.is_valid():
    #                             price_control = PRICE_CONTROL.objects.create(ProductID=product)
    #                             print("price_control:", price_control)
    #                             # price_control.Upper_Price = self.form_class_set_price(request.POST)
    #                             # price_control.Lower_Price = self.form_class_set_price(request.POST)
    #                             form_set_price.save()
    #                             # price_control.save()
                                
    #                             print("product.ProductID:", product.ProductID)
    #                             print("product_name:", product_name)
    #                             return redirect('my_app:Set_Price_List')
    #                         else:
    #                             # messages.error(request, f"Prices for {product.productName} not set.")
    #                             print("price_control_exists FAILED:", f"Prices for {product.productName} not set.")
    #                             return redirect('my_app:Set_Price_List')
    #             else:
    #                 # message = messages.error(request, f"Farmer offered Price for {product.productName} are not exists.")
    #                 print("farmer_offered_price_exists:", f"Farmer offered Price for {product.productName} not exists.")
    #                 return redirect('my_app:Set_Price_List')




    #             set_price_list = Farmer_Offered_Price.objects.all()
    #             return render(request, self.template_name, {'form': form, 'form_set_price': form_set_price, 'selected_product': product, 'Offered_Price_List': offered_price_list, 'Set_Price_List': set_price_list})

    #         return render(request, self.template_name, {'form': form})

'''
class SetPriceListViewAndCreateView(View):
    template_name = 'tables.html'
    form_class = SetPriceLocationForm
    form_class_set_price = SetPriceForm
    model = PRICE_CONTROL

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        set_price_list = Farmer_Offered_Price.objects.all()
        return render(request, self.template_name, {'form': form, 'Set_Price_List': set_price_list})



    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            # return redirect('my_app:Set_Price_List')

        product_name = form.cleaned_data.get('product')
        product = get_object_or_404(Product, productName=product_name)

        farmer_offered_price_exists = Farmer_Offered_Price.objects.filter(ProductID=product).exists()
        print("farmer_offered_price_exists:", farmer_offered_price_exists)

        if farmer_offered_price_exists:
            offered_price_list = Farmer_Offered_Price.objects.filter(ProductID=product.ProductID)
            print("product.ProductID:", product.ProductID)
            form_set_price = self.form_class_set_price()

            return render(request, self.template_name, {'form': form, 'form_set_price': form_set_price, 'selected_product': product, 'Offered_Price_List': offered_price_list, 'Set_Price_List': offered_price_list})
        else:
            # messages.error(request, f"Farmer offered Price for {product.productName} does not exist.")
            print("farmer_offered_price_exists:", f"Farmer offered Price for {product.productName} does not exist.")
            return redirect('my_app:Set_Price_List')

    def second_post(self, request, *args, **kwargs):
        print("Request POST:", request.POST)
        # Retrieve the selected product passed from the post method
        product = kwargs.get('selected_product')
    
        form = self.form_class_set_price(request.POST)
    
        if form.is_valid():
            # Check if there is an existing PRICE_CONTROL entry for the selected product
            price_control_exists = PRICE_CONTROL.objects.filter(ProductID=product).exists()
            print("price_control_exists:", price_control_exists)
            if price_control_exists:
                messages.error(request, f"Prices for {product.productName} are already set.")
            else:
                form.instance.ProductID = product
                form.save()
                return redirect('my_app:Set_Price_List')
        else:
            # Print form errors for debugging
            print(form.errors)
    
        # Render the form with errors and other necessary data
        set_price_list = Farmer_Offered_Price.objects.all()
        return render(request, self.template_name, {'form': form, 'Set_Price_List': set_price_list, 'selected_product': product})
'''
class SetPriceListViewAndCreateView(View):
    template_name = 'tables.html'
    form_class = SetPriceLocationForm
    form_class_set_price = SetPriceForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        set_price_list = Farmer_Offered_Price.objects.all()
        return render(request, self.template_name, {'form': form, 'Set_Price_List': set_price_list})
    '''
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        
        print("Request POST:", request.POST)

        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('product')
            print("product_name:", product_name)
            product = get_object_or_404(Product, productName=product_name)

            farmer_offered_price_exists = Farmer_Offered_Price.objects.filter(ProductID=product).exists()
            print("farmer_offered_price_exists:", farmer_offered_price_exists)

            if farmer_offered_price_exists:
                offered_price_list = Farmer_Offered_Price.objects.filter(ProductID=product.ProductID)
                form_set_price = self.form_class_set_price()

                # Process the second form
                form_set_price = self.form_class_set_price(request.POST)

                if form_set_price.is_valid():
                    # Check if there is an existing PRICE_CONTROL entry for the selected product
                    price_control_exists = PRICE_CONTROL.objects.filter(ProductID=product).exists()

                    if price_control_exists:
                        messages.error(request, f"Prices for {product.productName} are already set.")
                    else:
                        form_set_price.instance.ProductID = product
                        form_set_price.save()
                        return redirect('my_app:Set_Price_List')
                else:
                    # Print form errors for debugging
                    print(form_set_price.errors)

                return render(request, self.template_name, {'form': form, 'form_set_price': form_set_price, 'selected_product': product, 'Offered_Price_List': offered_price_list, 'Set_Price_List': offered_price_list})
            else:
                print(f"Farmer offered Price for {product.productName} does not exist.")
                return redirect('my_app:Set_Price_List')

        else:
            return render(request, self.template_name, {'form': form, 'Set_Price_List': Farmer_Offered_Price.objects.all()})'''


    
    def post(self, request, *args, **kwargs):
        # Determine target form based on POST data
        target_form = None
        if 'product' in request.POST:
            target_form = self.form_class(request.POST)
        elif 'set_price' in request.POST:
            target_form = self.form_class_set_price(request.POST)

        print("Request POST:", request.POST)
        
        # Handle form validation and processing for both cases
        if target_form and target_form.is_valid():
            # Form logic specific to each case
            if isinstance(target_form, self.form_class):
                # Logic for first form and saving product
                target_form.save()
                # ... additional logic ...
            elif isinstance(target_form, self.form_class_set_price):
                # Logic for second form and setting price
                target_form.instance.ProductID = kwargs.get('selected_product')
                print("target_form.instance.ProductID:", target_form.instance.ProductID)
                target_form.save()
                # ... additional logic ...
    
            return redirect('my_app:Set_Price_List')
    
        # Handle invalid forms or no target form identified
        else:
            # Get product based on kwargs if available for rendering
            product = kwargs.get('selected_product')
            
    
            # Check if first form validation is needed
            if isinstance(target_form, self.form_class):
                product_name = target_form.cleaned_data.get('product')
                product = get_object_or_404(Product, productName=product_name)
                print("product_name:", product_name)
                farmer_offered_price_exists = Farmer_Offered_Price.objects.filter(ProductID=product_name).exists()
                print(Farmer_Offered_Price.objects.all())
                print("farmer_offered_price_exists:", farmer_offered_price_exists)
                offered_price_list = Farmer_Offered_Price.objects.filter(ProductID=product.ProductID)
                print("product.ProductID:", product.ProductID)
                form_set_price = self.form_class_set_price()
                return render(request, self.template_name, {'form': self.form_class, 'form_set_price': form_set_price, 'selected_product': product, 'Offered_Price_List': offered_price_list, 'Set_Price_List': offered_price_list})
    
            # Prepare data for rendering based on target form
            offered_price_list = None
            set_price_list = None
            if product:
                print("product:", product)
                offered_price_list = Farmer_Offered_Price.objects.filter(ProductID=product.ProductID)
                set_price_list = offered_price_list
    
            # Choose the appropriate form object to render
            if target_form is None or isinstance(target_form, self.form_class):
                target_form = self.form_class()
            else:
                target_form = self.form_class_set_price()
    
            # Render template with forms and other data
            return render(request, self.template_name, {
                'form': target_form,
                'selected_product': product,
                'Offered_Price_List': offered_price_list,
                'Set_Price_List': set_price_list,
            })
    


'''
class SetPriceListViewAndCreateView(FormView):
    template_name = 'tables.html'
    form_class = SetPriceLocationForm
    model = PRICE_CONTROL
    success_url = reverse_lazy('my_app:Set_Price_List')
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        set_price_list = Farmer_Offered_Price.objects.all()
        return render(request, self.template_name, {'form': form, 'Set_Price_List': set_price_list})

    def form_valid(self, form):
        product_id = self.request.POST.get('product_id')
        print("product_iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii:", product_id)
        product = get_object_or_404(Product, ProductID=product_id)
        offered_price_exists = Farmer_Offered_Price.objects.filter(ProductID=product).exists()

        if offered_price_exists:
            messages.success(self.request, f"Product {product.productName} has existing farmer-offered prices.")
            return self.render_to_response(self.get_context_data(form=form, show_second_form=True, product=product))
        else:
            messages.error(self.request, f"Product {product.productName} has no farmer-offered prices.")
            return self.form_invalid(form)
    
    def form_valid(self, form):
        # Save the first form (SetPriceLocationForm)
        response = super().form_valid(form)
        
        # Check if the submit button for the second form is present in the POST data
        if 'show_second_form' in self.request.POST:
            product_id = self.request.POST.get('product_id')
            product = get_object_or_404(Product, ProductID=product_id)
            form_set_price = SetPriceForm(self.request.POST)

            if form_set_price.is_valid():
                form_set_price.instance.ProductID = product
                form_set_price.save()
                messages.success(self.request, f"Prices for {product.productName} have been set.")
                return response

            else:
                messages.error(self.request, "Invalid form submission for setting prices.")
                print("Form errors:", form_set_price.errors)
                return self.form_invalid(form_set_price)

        return response
        

    def form_invalid(self, form):
        # print("product_iddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd:")
        return self.render_to_response(self.get_context_data(form=form, show_second_form=False))

    def post(self, request, *args, **kwargs):
        form = self.get_form()
    
        print("Request POST:", request.POST)  # Print the entire request.POST content
    
        # Extract product ID if available
        product_id = request.POST.get('product_id')
        print("product_id:", product_id)
    
        if 'show_second_form' in request.POST:
            form_set_price = SetPriceForm(request.POST)
            if form_set_price.is_valid():
                # Use extracted product ID or fetch based on form data
                product = get_object_or_404(Product, ProductID=product_id or form_set_price.cleaned_data['product_id'])
                form_set_price.instance.ProductID = product
                form_set_price.save()
                messages.success(request, f"Prices for {product.productName} have been set.")
                return redirect('my_app:Set_Price_List')
            else:
                messages.error(request, "Invalid form submission for setting prices.")
                print("Form errors:", form_set_price.errors)
                return self.form_invalid(form)
    
        # Handle other form submissions (e.g., product selection)
        return super().post(request, *args, **kwargs)





    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Set_Price_List'] = PRICE_CONTROL.objects.all()
        return context

'''

# class SetPriceListViewAndCreateView(View):
#     template_name = 'tables.html'
#     form_class = SetPriceLocationForm
#     form_class_set_price = SetPriceForm

#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         form_set_price = self.form_class_set_price()
#         set_price_list = Farmer_Offered_Price.objects.all()
#         return render(request, self.template_name, {'form': form, 'form_set_price': form_set_price, 'Set_Price_List': set_price_list})

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             form.save()
#             product_name = form.cleaned_data.get('product', None)
#             product = get_object_or_404(Product, productName=product_name)

#             farmer_offered_price_exists = Farmer_Offered_Price.objects.filter(ProductID=product).exists()

#             if farmer_offered_price_exists:
#                 offered_price_list = Farmer_Offered_Price.objects.filter(ProductID=product.ProductID)
#                 print("product.ProductID:", product.ProductID)
#                 price_control_exists = PRICE_CONTROL.objects.filter(ProductID=product).exists()

#                 if price_control_exists:
#                     price_control = PRICE_CONTROL.objects.get(ProductID=product.ProductID)
#                     return render(
#                         request,
#                         self.template_name,
#                         {'form': form, 'selected_product': product, 'Offered_Price_List': offered_price_list, 'Price_Control': price_control}
#                     )
#                 else:
#                     messages.error(request, f"Prices for {product.productName} are not set.")
#             else:
#                 messages.error(request, f"Farmer offered Price for {product.productName} does not exist.")

#         return render(request, self.template_name, {'form': form})




def load_products(request):
    supplier_id = request.GET.get("supplier")
    products = Product.objects.filter(supplierID=supplier_id)
    return render(request, "products_options.html", {"products": products})
