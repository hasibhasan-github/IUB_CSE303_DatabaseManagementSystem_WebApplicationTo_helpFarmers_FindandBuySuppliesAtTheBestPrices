from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from Supplier.models import sTable
from Farmer.models import fTable
from testserver.views import dataPassingOverSeas
from Farmer.views import dataPassingOverSeasFarmer

# Create your views here.
class LandingPageView(TemplateView):
    template_name = 'LandingPage/LandingPage.html'

# class TestView(TemplateView):
#     template_name = 'testserver/base.html'

def register(request):
    msg = None 
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            # form.save()
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            gender = form.cleaned_data['gender']
            house = form.cleaned_data['house']
            street = form.cleaned_data['street']
            thana = form.cleaned_data['thana']
            zip_code = form.cleaned_data['zip']
            city = form.cleaned_data['city']
            contact_number = form.cleaned_data['contactnumber']
            supplier_type = form.cleaned_data['supplierType']
            user_type = form.cleaned_data['user_type']

            if user_type == "supplier":
                sTable.objects.create(
                    email=email,
                    fname=fname,
                    lname=lname,
                    gender=gender,
                    house=house,
                    street=street,
                    thana=thana,
                    zip=zip_code,
                    city=city,
                    contactnumber=contact_number,
                    supplierType=supplier_type,
                )
            else:
                fTable.objects.create(
                    email=email,
                    fname=fname,
                    lname=lname,
                    gender=gender,
                    house=house,
                    street=street,
                    thana=thana,
                    zip=zip_code,
                    city=city,
                    contactnumber=contact_number,
                )

            user = get_user_model().objects.create_user(
                username  = username,
                password = password,
                email = email ,
                first_name = fname,
                last_name = lname,
                user_type = user_type,
            )

            msg = 'user created'
            #return redirect('login_view')
            return render(request, 'LandingPage/LandingPage.html')
        else:
            msg = 'form is not Valid'
    else:
        form = SignUpForm()
    return render(request, 'LandingPage/register.html', {"form" : form, "msg" : msg})



# @login_required
def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None 
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            # print(user)
            if user is not None:
                login(request, user)
                # print(request.user.user_type)
                if request.user.user_type == "supplier":
                    # print(user.get_username())
                    dataPassingOverSeas(user.get_username())
                    return redirect('testserver/')
                elif request.user.user_type == "farmer":
                    dataPassingOverSeasFarmer(user.get_username)
                    return redirect('Farmer/')
                else:
                    msg = "User doesn't exits!"
                # return redirect('testserver/')
            else:
                msg = "invalid credentials"
        else:
            msg = "Error validating form"
    return render(request, 'LandingPage/loginmain.html', {'form':form, 'msg':msg})






def logout_view(request):
    logout(request)
    return redirect(reverse('LandingPage/LandingPage.html'))


