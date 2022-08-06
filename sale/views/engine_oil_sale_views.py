from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from ..models import EngineOilSale
from ..forms import EngineOilSaleForm


def engine_oil_sale_list(request):

    sales = EngineOilSale.objects.filter(status=True).order_by('-date').all()
    for sale in sales:
        print(sale.date)
    context = {'sales':sales}
    return render(request, 'sale/engine-oil/list.html', context=context)

def add_engine_oil_sale(request):

    form = EngineOilSaleForm(initial={'discount':0})
    if request.method == "POST":
        form = EngineOilSaleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Engine oil sale added successfully!')
            return redirect('sale:engine_oil_sale_list')
        else:
            messages.error(request, form.errors)
    context = {'form':form}
    return render(request, 'sale/engine-oil/create.html', context=context)

def update_engine_oil_sale(request, pk):

    sale = get_object_or_404(EngineOilSale, id=pk)
    form = EngineOilSaleForm(instance=sale)
    if request.method == "POST":
        form = EngineOilSaleForm(request.POST, instance=sale)
        if form.is_valid():
            form.save()
            messages.success(request, 'Engine oil sale updated successfully!')
            return redirect('sale:engine_oil_sale_list')
        else:
            messages.error(request, form.errors)
    context = {'form':form, 'sale':sale}
    return render(request, 'sale/engine-oil/update.html', context=context)