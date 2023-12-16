from django.urls import path
from . import views

urlpatterns = [
    path('fp/', views.Financial_plan),
    
]
