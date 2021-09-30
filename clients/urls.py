from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('<int:user_id>/company_dashboard/', views.dashboard, name='company dashboard'),all_customer
    path('company_dashboard/', views.dashboard, name='company dashboard'),
    path('product/', views.product, name='product upload'),
    path('menu/', views.my_menu, name='my menu'),
    path('add_customer/', views.add, name='new customer'),
    path('all_customer/', views.all_customer, name='all customer'),
    path('deleting_customer/<int:key_id>', views.delete_customer, name='delete customer'),
    path('offers/', views.offers, name='offers'),
    path('theme/<int:theme_id>', views.select_theme, name='select_theme'),
]