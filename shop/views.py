from django.shortcuts import render, redirect
from .models import Category, Product, Order
from django.contrib import messages
# Create your views here.

def get_naviget_item():
    return Category.objects.all()

def home(request):
    
    category = get_naviget_item()
    context = {
        'category':category
    }

    return render(request, 'home.html', context)


def shop(request):
    filter_value = request.GET.get('filter')
    product = Product.objects.select_related("category")
    if filter_value:
        category_id = Category.objects.get(name=filter_value)
        product = product.filter(category=category_id)
    else:
        product = product.all().order_by('-id')
    category = get_naviget_item()
    context = {
        'category':category,
        'product':product
    }
    return render(request, 'shop.html', context)


def single_product(request, slug):
    category = get_naviget_item()
    data = Product.objects.get(slug=slug)
    context = {
        'category':category,
        'data':data
    }
    return render(request, 'single_product.html', context)


def confirm_order(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        delivery_area = request.POST.get('delivery_area')
        slug = request.POST.get('slug')
        quantity = request.POST.get('quantity')
        
        items = Product.objects.get(slug=slug)
        
        order_info = Order (
            customar_name = name,
            phone_number = phone,
            address = address,
            location_area = delivery_area,
            items = items,
            quentity = quantity
        )
        if delivery_area == 'Inside':
            order_info.delivery_charge = 50
        else:
            order_info.delivery_charge = 100
        
        order_info.save()
        messages.success(request, 'Your Order Successfully confirm')
        return redirect('shop:home')
        
    else:
        return redirect('shop:home')