from django.shortcuts import render
from .models import Product, ProductCategory

# Create your views here.

def product_list(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'product/list.html', context=context)