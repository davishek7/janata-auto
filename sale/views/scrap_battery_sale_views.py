from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from ..models import ScrapBatterySale, jsonfield_default_value  
from ..forms import ScrapBatterySaleForm


def scrap_battery_sale_list(request):

    scrap_batteries = ScrapBatterySale.objects.filter(status = True).order_by('-date').all()
    context = {'scrap_batteries':scrap_batteries}
    return render(request, 'sale/scrap-battery/list.html', context=context)

def add_scrap_battery_sale(request):

    form = ScrapBatterySaleForm(initial={'items':jsonfield_default_value})
    if request.method == "POST":
        form = ScrapBatterySaleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Scrap battery sale added successfully!')
            return redirect('sale:scrap_battery_sale_list') 
        else:
            messages.error(request, form.errors)
    context = {'form':form}
    return render(request, 'sale/scrap-battery/create.html', context=context)

def update_scrap_battery_sale(request, pk):

    sale = get_object_or_404(ScrapBatterySale, id=pk)
    form = ScrapBatterySaleForm(instance=sale)
    if request.method == "POST":
        form = ScrapBatterySaleForm(request.POST, instance=sale)
        if form.is_valid():
            form.save()
            messages.success(request, 'Scrap battery sale updated successfully!')
            return redirect('sale:scrap_battery_sale_list') 
        else:
            messages.error(request, form.errors)
    context = {'form':form}
    return render(request, 'sale/scrap-battery/update.html', context=context)