from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, FormView, CreateView
from testserver.forms import Testform

from testserver.models import Test

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



