from django.urls import path
from . import views

urlpatterns = [
    path('', views.Financial_plan),
    
]
