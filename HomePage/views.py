from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from django.contrib import auth, messages
from django.urls import reverse_lazy
from HomePage.models import CustomUserCreationForm, Suppliers

# Create your views here.

class LandingPageView(TemplateView):
    template_name = 'HomePage/LandingPage.html'




