from django.urls import path
from . import views
app_name = 'shop'


urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('singl-product/<slug>/', views.single_product, name='single_product'),
] 
