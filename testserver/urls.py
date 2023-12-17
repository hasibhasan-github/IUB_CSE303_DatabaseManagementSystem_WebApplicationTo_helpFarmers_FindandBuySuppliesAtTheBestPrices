from django.urls import path 
from .views import TestView, ThankuView, TestForm, TestCreateView, TestProductCreateView, TestProductListView, test_view, ProfileView, ProductDetailView, ProductUpdateView, ProductDeleteView, OrderListView
from . import views

app_name = 'testserver'

urlpatterns = [
    path('', test_view, name='test'),
    path('thanku/', ThankuView.as_view(), name='thanku'),
    path('profile/', ProfileView, name='profile'),
    path('testform/', TestForm.as_view(), name='testform'),
    path('testform2/', TestCreateView.as_view(), name='testform2'),
    path('product/', TestProductCreateView.as_view(), name='product'),
    path('productlist/', TestProductListView.as_view(), name='productlist'),
    path('orderlist/', OrderListView.as_view(), name='orderlist'),
    path('productupdateview/<int:pk>/', ProductUpdateView.as_view(), name='productupdate'),
    path('productdeleteview/<int:pk>/', ProductDeleteView.as_view(), name='productdelete'),
]