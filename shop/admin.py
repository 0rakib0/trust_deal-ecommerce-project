from django.contrib import admin
from .models import Category, Product, Order
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('items', 'quentity', 'customar_name', 'address', 'location_area', 'is_deliverd', 'order_date')

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order, OrderAdmin)
