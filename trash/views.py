from django.shortcuts import render, redirect, get_object_or_404
from vendor.models import Vendor
from product.models import Product
from django.contrib import messages

# Create your views here.

def deleted_vendors(request):

    vendors = Vendor.objects.filter(status=False)
    context = {'vendors':vendors}
    return render(request, 'trash/vendors/list.html', context=context)

def restore_vendor(request, pk):

    vendor = get_object_or_404(Vendor, id=pk)
    vendor.status = True
    vendor.save()
    messages.success(request, f'{vendor} restored successfully!')
    return redirect('vendor:list')

def deleted_products(request):

    products = Product.objects.filter(status=False)
    context = {'products':products}
    return render(request, 'trash/products/list.html', context=context)

def restore_product(request, pk):

    product = get_object_or_404(Product, id=pk)
    product.status = True
    product.save()
    messages.success(request, f'{product} restored successfully!')
    return redirect('product:list')