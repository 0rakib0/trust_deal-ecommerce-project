from django.urls import path
from . import views
app_name = 'shop'


urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('singl-product/<slug>/', views.single_product, name='single_product'),
    path('confirm-order/', views.confirm_order, name='confirm_order'),
    path('find-items/', views.serach_items, name='search_item')
] 
