from django.urls import path 
from .views import TestView, ThankuView, TestForm, TestCreateView


app_name = 'testserver'

urlpatterns = [
    path('', TestView.as_view(), name='test'),
    path('thanku/', ThankuView.as_view(), name='thanku'),
    path('testform/', TestForm.as_view(), name='testform'),
    path('testform2/', TestCreateView.as_view(), name='testform2'),
]