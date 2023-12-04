from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def Contact(request):
    return render(request,'Contact/contact.html')

# def studio(request):
#     return render(request,'machine_learning/studio.html')

# def black_forest(request):
#     return render(request,'machine_learning/black_forest.html')

# def AK_47(request):
#     return render(request,'machine_learning/AK-47.html')











# def deep_learning(request):
#     return HttpResponse('<h1>Welcome to Binary_Bots Website. This is my 2nd function.</h1>')





# def shayra(request):
#     return HttpResponse('Its a trap!')

# def masum(request):
#     return HttpResponse('<h1>It will be good, if I never let you back in my life<h1>')