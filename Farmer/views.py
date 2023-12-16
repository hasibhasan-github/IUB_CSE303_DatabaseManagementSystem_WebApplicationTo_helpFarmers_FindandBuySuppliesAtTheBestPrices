from django.shortcuts import render

# Create your views here.

def view(request):
    template_name = 'Farmer/a.html'
    return render(request, template_name)
