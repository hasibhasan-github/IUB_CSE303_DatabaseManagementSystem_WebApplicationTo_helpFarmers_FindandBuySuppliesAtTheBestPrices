from django.urls import path 
from .views import TestView, ThankuView, TestForm, TestCreateView, TestProductCreateView, TestProductListView
from . import views

app_name = 'testserver'

urlpatterns = [
    path('', TestView.as_view(), name='test'),
    path('thanku/', ThankuView.as_view(), name='thanku'),
    path('testform/', TestForm.as_view(), name='testform'),
    path('testform2/', TestCreateView.as_view(), name='testform2'),
    path('product/', TestProductCreateView.as_view(), name='product'),
    path('productlist/', TestProductListView.as_view(), name='productlist'),
]