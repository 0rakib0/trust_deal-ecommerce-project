from django.shortcuts import render
from .models import Category
# Create your views here.
def home(request):
    category = Category.objects.all()
    context = {
        'category':category
    }

    return render(request, 'home.html', context)
