from django.urls import path
from . import views

urlpatterns = [
    path('rn/', views.Research_news),
    
]
