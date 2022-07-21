from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from ..models import DistilledWater
from ..forms import DistilledWaterCreateForm, DistilledWaterUpdateForm


def distilled_water_list(request):

    distilled_waters = DistilledWater.objects.filter(status=True)
    context = {'distilled_waters':distilled_waters}
    return render(request, 'asset/distilled-water/list.html', context=context)

def add_distilled_water(request):

    form = DistilledWaterCreateForm()
    if request.method == "POST":
        form = DistilledWaterCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Distilled water added successfully!')
            if request.POST.get('save-list'):
                return redirect('asset:distilled_water_list')
            elif request.POST.get('save-add'):
              return redirect(request.META.get('HTTP_REFERER')) 
        else:
            messages.error(request, form.errors)
    context = {'form':form}
    return render(request, 'asset/distilled-water/create.html', context=context)

def update_distilled_water(request, pk):

    distilled_water = get_object_or_404(DistilledWater, id=pk)
    form = DistilledWaterUpdateForm(instance=distilled_water)
    if request.method == "POST":
        form = DistilledWaterUpdateForm(request.POST, instance=distilled_water)
        if form.is_valid():
            form.save()
            messages.success(request, f'{distilled_water} updated successfully!')
            return redirect('asset:distilled_water_list')
        else:
            messages.error(request, form.errors)
    context = {'form':form, 'distilled_water':distilled_water}
    return render(request, 'asset/distilled-water/update.html', context=context)