from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import userFrom
from .models import Cart
from django.shortcuts import get_object_or_404
from Supplier.models import sTable
from Product.models import pTable
from Farmer.models import fTable
from Order.models import oTable
from testserver.models import bug2
from LandingPage.models import User


# Create your views here.



# Start
def bugg(loggedinperson):
    bug_instance, created = bug2.objects.get_or_create(id=784)
    if not created:
        bug_instance.user = loggedinperson
        bug_instance.save() 
    else:
        bug2.objects.create()



bugg("FarmerNormal")


def get_supplier_by_username(email):
    supplier = get_object_or_404(User, email=email)
    bugg(supplier.pk)

def get_user_by_username(username):
    supplier = get_object_or_404(User, username=username)
    get_supplier_by_username(supplier.email)


def dataPassingOverSeasFarmer(username):
    get_user_by_username(username)
# End






def base(request):
    return render(request, ('Farmer/base.html'))

def page_view(request):
    return render(request, ('Farmer/index.html'))

def priceOffer(request):
    return render(request, ('Farmer/priceOffer.html'))

def consultancy(request):
    return render(request, ('Farmer/consultancy.html'))
   
   
def order(request):
    pass

# def order(request):
#     total = 0
#     data = {}
#     cart_items = Cart.objects.all()
#     supplier_model = supplier.objects.all()
#     product_model = product.objects.all()

#     data['product_model'] = product_model
#     data['supplier_model'] = supplier_model

#     try:
#         if request.method == 'POST':
#             supp = request.POST['supplier_type']
#             pro = request.POST['product_name']
#             quantity = int(request.POST['quantity'])

            

#             selected_product = product.objects.get(productName=pro)
            

#             total = quantity * selected_product.productPrice
#             print(total)

#             # Add the new item to the cart
#             Cart.objects.create(
#                 supplier=supp,
#                 product=pro,
#                 quantity=quantity,
#                 totalPrice=total
#             )
#             data['cart_items'] = cart_items

#     except Exception as e:
#         print(e)

#     delivery_charge = 50
#     final_total = delivery_charge + total

#     data['total'] = total
#     data['delivery_charge'] = delivery_charge
#     data['final_total'] = final_total


#     return render(request, 'mainSite/order.html', data)


def order(request):
    total = 0
    data = {}
    cart_items = Cart.objects.all()
    supplier_model = sTable.objects.all()
    product_model = pTable.objects.all()

    data['product_model'] = product_model
    data['supplier_model'] = supplier_model

    try:
        if request.method == 'POST':
            action = request.POST.get('action')

            if action == 'add_to_cart':
                # Add to Cart logic
                supp = request.POST['supplier_type']
                pro = request.POST['product_name']
                quantity = int(request.POST['quantity'])

                selected_product = pTable.objects.get(productName=pro)

                total = quantity * selected_product.productPrice

                # Add the new item to the cart
                Cart.objects.create(
                    supplier=supp,
                    product=pro,
                    quantity=quantity,
                    totalPrice=total
                )
                print(supp)

            elif action == 'place_order':



                Cart.objects.all().delete()
                
               

    except Exception as e:
        print(e)

    delivery_charge = 50
    final_total = delivery_charge + total


    data['cart_items'] = cart_items
    data['total'] = total
    data['delivery_charge'] = delivery_charge
    data['final_total'] = final_total

    return render(request, 'mainSite/order.html', data)



def form(request):
    fn = userFrom()
    result = 0
    data = {'form': fn}
    try:
        if request.method == 'POST':
         s1 = int(request.POST['num1'])
         s2 = int(request.POST['num2'])
         result = s1 + s2
         data = {"form": fn,
                  "output":result}
        
        
    except:
        pass

    
    return render(request, 'mainSite/h.html',data)



