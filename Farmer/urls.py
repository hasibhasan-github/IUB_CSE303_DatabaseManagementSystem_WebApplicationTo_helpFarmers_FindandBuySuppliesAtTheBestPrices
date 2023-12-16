from django.urls import path
from . import views

app_name = 'Farmer'



urlpatterns = [
   path('',views.page_view,name="dashboard"),
   path('order/', views.order,name="order"),
   path('priceOffer/', views.priceOffer,name="priceOffer"),
   path('consultancy/', views.consultancy,name="consultancy"),
   path('base/', views.base),
   path('form/', views.form),
]
 