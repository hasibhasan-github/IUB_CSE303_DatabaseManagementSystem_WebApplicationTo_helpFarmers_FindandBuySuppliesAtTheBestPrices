from django.shortcuts import render

# Create your views here.


def view(request):
    return render(request, 'ARDOfficer/Consultant_Dashboard.html')

def base(request):
     return render(request, ('ARDOfficer/base.html'))

def Contact(request):
    return render(request, ('ARDOfficer/contact.html'))

def Research_news(request):
    return render(request, ('ARDOfficer/research_news.html'))

def Farmer_data(request):
    return render(request, ('ARDOfficer/Farmer_data.html'))

def Financial_plan(request):
     return render(request, ('ARDOfficer/Financial_Plan.html'))
