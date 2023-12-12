from django.urls import path 
from .views import LandingPageView #SignUpView, CustomLoginView
from . import views

app_name = 'LandingPage'

urlpatterns = [
    path('', LandingPageView.as_view(), name='LandingPage'), 
    path('signup/', views.register, name='signup'),
    path('login/', views.login_view, name='loginmain'),
    path('logout/', views.logout_view, name='logout'),
    # path('signup/', SignUpView.as_view(), name='signup'),
    # path('login/', CustomLoginView.as_view(), name='login'),

]