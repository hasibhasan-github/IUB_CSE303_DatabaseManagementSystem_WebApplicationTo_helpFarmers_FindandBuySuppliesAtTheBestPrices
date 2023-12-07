from django.urls import path 
from .views import LandingPageView
from . import views

app_name = 'HomePage'

urlpatterns = [
    path('', LandingPageView.as_view(), name='LandingPage'),
]