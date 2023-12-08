from django.urls import path 
from .views import LandingPageView, SignUpView, CustomLoginView
from . import views

app_name = 'HomePage'

urlpatterns = [
    # path('', LandingPageView.as_view(), name='LandingPage'), 
    # path('signup/', SignUpView.as_view(), name='signup'),
    # path('signup/', CustomLoginView.as_view(), name='signup'),
    # path('', views.loginseen, name='loginpage'),
]