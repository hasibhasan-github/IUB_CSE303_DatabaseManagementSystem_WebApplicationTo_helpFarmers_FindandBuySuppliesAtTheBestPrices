from django.urls import path 
from .views import view
from . import views

app_name = 'testserver'

urlpatterns = [
    path('', view, name='view'),

]