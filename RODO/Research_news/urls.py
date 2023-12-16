from django.urls import path
from . import views

urlpatterns = [
    path('rn/', views.Research_news),
    path('rnc/', views.Research_news1.as_view())
]
