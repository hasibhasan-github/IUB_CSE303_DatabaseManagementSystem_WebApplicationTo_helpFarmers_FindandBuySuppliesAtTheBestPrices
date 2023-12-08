from django.urls import path
from . import views
from .views import DashboardView, SetPriceListView, SetPriceCreateView

app_name = 'my_app'

# urlpatterns = [
#     path('', dashboard, name='Dashboard'),
#     path('pages/dashboard.html', views.dashboard, name='Dashboard'),
#     path('pages/tables.html', views.table, name='Table'),
#     path('pages/notifications.html', views.notifications, name='Notifications'),
#     path('pages/profile.html', views.profile, name='Profile'),
#     path('pages/sign_out.html', views.sign_out, name='sign_out'),
# ]
# urlpatterns = [
#     path('', SetPriceCreateView.as_view(), name='Set_Price'),
#     path('', SetPriceListView.as_view(), name='Set_Price_List'),
#     path('', DashboardView.as_view(), name='Dashboard'),
# ]

urlpatterns = [
    path('', DashboardView.as_view(), name='Dashboard'),
    path('dashboard/', DashboardView.as_view(), name='Dashboard'),
    path('set_price_list/', SetPriceListView.as_view(), name='Set_Price_List'),
    path('set_price/', SetPriceCreateView.as_view(), name='Set_Price'),
]

