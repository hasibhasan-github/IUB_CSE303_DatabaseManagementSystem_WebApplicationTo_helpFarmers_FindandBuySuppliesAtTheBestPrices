from django.urls import path 
from ARDOfficer.views import view 

app_name = 'ARDOfficer'

urlpatterns = [
    path('', view, name='view'), 

]