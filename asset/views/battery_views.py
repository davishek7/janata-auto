from django.shortcuts import render, redirect
from django.contrib import messages
from ..models import Battery, EngineOil, DistilledWater
from ..forms import BatteryCreateForm


def battery_list(request):
    batteries = Battery.objects.all()
    context = {'batteries':batteries}
    return render(request, 'asset/battery/list.html', context=context)

def add_battery(request):
    form = BatteryCreateForm()
    if request.method == "POST":
        form = BatteryCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added.')
            if request.POST.get('save-list'):
                return redirect('asset:battery_list')
            elif request.POST.get('save-add'):
              return redirect(request.META.get('HTTP_REFERER'))  
        else:
            messages.error(request, formset.errors)
            return redirect(request.META.get('HTTP_REFERER'))
    context = {'form':form}
    return render(request, 'asset/battery/create.html', context=context)
