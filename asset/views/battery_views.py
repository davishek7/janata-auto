from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from ..models import Battery
from ..forms import BatteryCreateForm, BatteryUpdateForm


def battery_list(request):

    batteries = Battery.objects.filter(status = True)
    context = {'batteries':batteries}
    return render(request, 'asset/battery/list.html', context=context)

def add_battery(request):

    form = BatteryCreateForm()
    if request.method == "POST":
        form = BatteryCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Battery asset added successfully!')
            if request.POST.get('save-list'):
                return redirect('asset:battery_list')
            elif request.POST.get('save-add'):
              return redirect(request.META.get('HTTP_REFERER'))  
        else:
            messages.error(request, form.errors)
    context = {'form':form}
    return render(request, 'asset/battery/create.html', context=context)

def update_battery(request, pk):

    battery = get_object_or_404(Battery, id=pk)
    form = BatteryUpdateForm(instance=battery)
    if request.method == "POST":
        form = BatteryUpdateForm(request.POST, instance=battery)
        if form.is_valid():
            form.save()
            messages.success(request, f'{battery} updated successfully!')
            return redirect('asset:battery_list')
        else:
            messages.error(request, form.errors)
    context = {'form':form, 'battery':battery}
    return render(request, 'asset/battery/update.html', context=context)