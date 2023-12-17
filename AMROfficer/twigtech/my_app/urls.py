from django.urls import path
from . import views
from .views import DashboardView, SetPriceListViewAndCreateView, DetailsView


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

# urlpatterns = [
#     path('Price_Control/', SetPriceListViewAndCreateView.as_view(), name='price_control'),
#     path('Price_Control/submit/', SetPriceListViewAndCreateView.as_view(), name='price_submit'),
# ]


urlpatterns = [
    path('', DashboardView.as_view(), name='Dashboard'),
    path('dashboard/', DashboardView.as_view(), name='Dashboard'),
    path('Price_Control/', SetPriceListViewAndCreateView.as_view(), name='Set_Price_List'),
    path('Price_Control/submit/', views.SetPriceListViewAndCreateView.as_view(), name='Set_Price_List'),
    path('Price_Control/', SetPriceListViewAndCreateView.as_view(), name='price_control'),
    path('Price_Control/submit/', SetPriceListViewAndCreateView.as_view(), name='price_submit'),
    path('', SetPriceListViewAndCreateView.as_view(), name='Set_Price_List'),
    path('Price_Control/', SetPriceListViewAndCreateView.as_view(), name='Set_Price_List'),
    path('Price_Control/submit/', SetPriceListViewAndCreateView.as_view(), name='second_post'),
    path("", views.book_search, name="load_books"),
    # path('Select_Supplier_Type_and_Product', views.index, name="index"),
    path('', DetailsView.as_view(), name='Details_View'),
    path("load_products/", views.load_products, name="load_products"),
    path("Price_Control/load_products/", views.load_products, name="load_products"),
    path('details/', DetailsView.as_view(), name='details'),
]

