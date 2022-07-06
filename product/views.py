from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product, ProductCategory
from .forms import ProductForm, ProductCategoryForm, ProductSizeForm

# Create your views here.

def product_list(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'product/list.html', context=context)

def add_product(request):

    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Products added successfully!')
            return redirect('product:list')
        else:
            messages.error(request, form.errors)
            return redirect(request.META.get('HTTP_REFERER'))
    context = {'form':form}
    return render(request, 'product/create.html', context=context)

def update_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    form = ProductForm(instance=product)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            messages.success(request, f'{product} updated successfully!')
            return redirect('product:list')
        else:
            messages.error(request, form.errors)
            return redirect(request.META.get('HTTP_REFERER'))
    context = {'form':form, 'product':product}
    return render(request, 'product/update.html', context=context)

def add_product_category(request):
    if request.method == "POST":
        c_form = ProductCategoryForm(request.POST)
        if c_form.is_valid():
            c_form.save()
            return redirect(request.META.get('HTTP_REFERER'))