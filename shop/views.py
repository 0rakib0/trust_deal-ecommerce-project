from django.shortcuts import render
from .models import Category, Product
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
