from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, FormView, CreateView, ListView
from testserver.forms import Testform

from testserver.models import Test, TestProduct

# Create your views here.

class TestView(TemplateView):
    template_name = 'testserver/base.html'

class ThankuView(TemplateView):
    template_name = 'testserver/thanku.html'

class TestForm(FormView):
    form_class = Testform
    template_name = 'testserver/product.html'

    success_url = "/thanku/"

    def form_valid(self, form):
        
        print(form.cleaned_data)
        return super().form_valid(form)
    

class TestCreateView(CreateView):
    model = Test 
    fields = "__all__"
    success_url = "/thanku/"


class TestProductCreateView(CreateView):
    model = TestProduct
    fields = ['prod_name', 'prod_price']
    success_url = "/thanku/"

    labels = {
            'prod_name': 'Product Name: ',
        }


class TestProductListView(ListView):
    model = TestProduct
    queryset = TestProduct.objects.order_by('prod_name')

    # context_object_name = "ProductList" // For changing object List

