from django.shortcuts import render, redirect
from django.contrib import messages
from ..models import Battery, EngineOil, DistilledWater
from ..forms import BatteryCreateForm, BatteryCreateFormSet


def battery_list(request):
    batteries = Battery.objects.all()
    context = {'batteries':batteries}
    return render(request, 'asset/battery/list.html', context=context)

def add_battery(request):
    formset = BatteryCreateFormSet(queryset = Battery.objects.none())
    if request.method == "POST":
        formset = BatteryCreateFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            messages.success(request, 'Successfully added.')
            return redirect('asset:battery_list')
        else:
            messages.error(request, formset.errors)
            return redirect(request.META.get('HTTP_REFERER'))
    context = {'formset':formset}
    return render(request, 'asset/battery/create.html', context=context)
