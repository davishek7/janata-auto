from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product, ProductCategory, ProductSize
from .forms import ProductForm, ProductCategoryForm, ProductSizeForm

# Create your views here.

def product_list(request):

    products = Product.objects.filter(status = True)
    context = {'products':products}
    return render(request, 'product/list.html', context=context)

def add_product(request):

    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully!')
            if request.POST.get('save-list'):
                return redirect('product:list')
            elif request.POST.get('save-add'):
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, form.errors)
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
    context = {'form':form, 'product':product}
    return render(request, 'product/update.html', context=context)

def delete_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    product.status = False
    product.save()
    messages.success(request, f'{product} deleted successfully!')
    return redirect('product:list')

def add_product_category(request):

    form = ProductCategoryForm()
    if request.method == "POST":
        form = ProductCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product category added successfully!')
            if request.POST.get('save-list'):
                return redirect('product:list_product_category')
            elif request.POST.get('save-add'):
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, form.errors)
    context = {'form':form}
    return render(request, 'product/category/create.html', context=context)

def list_product_category(request):

    categories = ProductCategory.objects.filter(status = True)
    context = {'categories':categories}
    return render(request, 'product/category/list.html', context=context)

def update_product_category(request, pk):

    category = get_object_or_404(ProductCategory, id=pk)
    form = ProductCategoryForm(instance=category)
    if request.method == "POST":
        form = ProductCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, f'{category} updated successfully!')
            return redirect('product:list_product_category')
        else:
            messages.error(request, form.errors)
    context = {'form':form, 'category':category}
    return render(request, 'product/category/update.html', context=context) 
    
def add_product_size(request):
    
    form = ProductSizeForm()
    if request.method == "POST":
        form = ProductSizeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product size added successfully!')
            if request.POST.get('save-list'):
                return redirect('product:list_product_size')
            elif request.POST.get('save-add'):
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, form.errors)
    context = {'form':form}
    return render(request, 'product/size/create.html', context=context)

def list_product_size(request):

    sizes = ProductSize.objects.filter(status = True)
    context = {'sizes':sizes}
    return render(request, 'product/size/list.html', context=context)

def update_product_size(request, pk):

    size = get_object_or_404(ProductSize, id=pk)
    form = ProductSizeForm(instance=size)
    if request.method == "POST":
        form = ProductSizeForm(request.POST, instance=size)
        if form.is_valid():
            form.save()
            messages.success(request, f'{size} updated successfully!')
            return redirect('product:list_product_size')
        else:
            messages.error(request, form.errors)
    context = {'form':form, 'size':size}
    return render(request, 'product/size/update.html', context=context) 