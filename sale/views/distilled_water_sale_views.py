from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from ..models import DistilledWaterSale
from ..forms import DistilledWaterSaleForm


def distilled_water_sale_list(request):

    sales = DistilledWaterSale.objects.filter(status=True).order_by('-date').all()
    for sale in sales:
        print(sale.date)
    context = {'sales':sales}
    return render(request, 'sale/distilled-water/list.html', context=context)

def add_distilled_water_sale(request):

    form = DistilledWaterSaleForm(initial={'discount':0})
    if request.method == "POST":
        form = DistilledWaterSaleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Distilled water sale added successfully!')
            return redirect('sale:distilled_water_sale_list')
        else:
            messages.error(request, form.errors)
    context = {'form':form}
    return render(request, 'sale/distilled-water/create.html', context=context)

def update_distilled_water_sale(request, pk):

    sale = get_object_or_404(DistilledWaterSale, id=pk)
    form = DistilledWaterSaleForm(instance=sale)
    if request.method == "POST":
        form = DistilledWaterSaleForm(request.POST, instance=sale)
        if form.is_valid():
            form.save()
            messages.success(request, 'Distilled water sale updated successfully!')
            return redirect('sale:distilled_water_sale_list')
        else:
            messages.error(request, form.errors)
    context = {'form':form, 'sale':sale}
    return render(request, 'sale/distilled-water/update.html', context=context)