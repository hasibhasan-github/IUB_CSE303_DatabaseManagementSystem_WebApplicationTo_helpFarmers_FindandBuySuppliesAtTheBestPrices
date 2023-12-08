from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model

# Create your views here.
class LandingPageView(TemplateView):
    template_name = 'LandingPage/LandingPage.html'

class TestView(TemplateView):
    template_name = 'testserver/base.html'

def register(request):
    msg = None 
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
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
            user_type = form.cleaned_data['userType']

            user = get_user_model().objects.create_user(
                username= username,
                email=email,
                password=password,
                first_name=fname,
                last_name=lname,
                gender=gender,
                house=house,
                street=street,
                thana=thana,
                zip=zip_code,
                city=city,
                contactnumber=contact_number,
                supplierType=supplier_type,
                userType=user_type,
            )

            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not Valid'
    else:
        form = SignUpForm()
    return render(request, 'LandingPage/register.html', {"form" : form, "msg" : msg})

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None 
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('testserver/')
            else:
                msg = "invalid credentials"
        else:
            msg = "Error validating form"
    return render(request, 'LandingPage/loginmain.html', {'form':form, 'msg':msg})



