from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, FormView, CreateView, ListView
from testserver.forms import Testform
from Supplier.models import sTable
from django.shortcuts import get_object_or_404
from LandingPage.models import User
from .models import bug
from Product.models import pTable
from testserver.models import Test
from django.urls import reverse_lazy

# Create your views here.

def bugg(loggedinperson):
    bug_instance, created = bug.objects.get_or_create(id=784)
    if not created:
        bug_instance.user = loggedinperson
        bug_instance.save() 
    else:
        bug.objects.create()


bugg("HasibNormal")


def get_supplier_by_username(email):
    supplier = get_object_or_404(User, email=email)
    bugg(supplier.pk)

def get_user_by_username(username):
    supplier = get_object_or_404(User, username=username)
    get_supplier_by_username(supplier.email)


def dataPassingOverSeas(username):
    get_user_by_username(username)
    # bugg(username)





#supplierInstance = get_user_by_username(userInstance.email)


class TestView(TemplateView):
    template_name = 'testserver/base.html'


def ProfileView(request):
    template_name = 'testserver/profile.html'

    bug_instance, created = bug.objects.get_or_create(id=784) 
    # print(sTable.objects.get_or_create(supplierID = bug_instance.user))
    
    if  bug_instance.user == 'HasibNormal':
        pass 
    else:
        s_table_instance, s_table_created = sTable.objects.get_or_create(supplierID=bug_instance.user)

    context = {
        's_table_instance': s_table_instance,
    }

    return render(request, template_name, context)


def test_view(request):
    template_name = 'testserver/base.html'

    bug_instance, created = bug.objects.get_or_create(id=784) 
    # print(sTable.objects.get_or_create(supplierID = bug_instance.user))
    
    if  bug_instance.user == 'HasibNormal':
        pass 
    else:
        s_table_instance, s_table_created = sTable.objects.get_or_create(supplierID=bug_instance.user)

    context = {
        's_table_instance': s_table_instance,
    }

    return render(request, template_name, context)


class ThankuView(TemplateView):
    template_name = 'testserver/thanku.html'

class TestForm(FormView):
    form_class = Testform
    template_name = 'TestView'

    success_url = reverse_lazy('thanku')

    def form_valid(self, form):
        
        print(form.cleaned_data)
        return super().form_valid(form)
    

class TestCreateView(CreateView):
    model = Test 
    fields = "__all__"
    success_url = "/thanku/"


class TestProductCreateView(CreateView):
    model = pTable
    fields = ['productName', 'productPrice']
    success_url = reverse_lazy('testserver:productlist')

    def form_valid(self, form):
        bug_instance, created = bug.objects.get_or_create(id=784) 
        
        if  bug_instance.user == 'HasibNormal':
            pass 
        else:
            s_table_instance, s_table_created = sTable.objects.get_or_create(supplierID=bug_instance.user)
        # Assign the supplier instance to the TestProduct before saving
        form.instance.supplierID  = s_table_instance

        # p_table_instance = form.save()
        # s_table_instance = sTable.objects.get(supplierID=form.instance.supplierID)

        return super().form_valid(form)



class TestProductListView(ListView):
    model = pTable
    # queryset = pTable.objects.order_by('productName')
    
    
    def get_queryset(self):
        bug_instance, created = bug.objects.get_or_create(id=784) 
        
        if  bug_instance.user == 'HasibNormal':
            pass 
        else:
            s_table_instance, s_table_created = sTable.objects.get_or_create(supplierID=bug_instance.user)

        queryset = pTable.objects.filter(supplierID =  s_table_instance.supplierID )

        return queryset


    # context_object_name = "ProductList" // For changing object List

