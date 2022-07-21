from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from ..models import EngineOil
from ..forms import EngineOilCreateForm, EngineOilUpdateForm


def engine_oil_list(request):

    engine_oils = EngineOil.objects.filter(status=True)
    context = {'engine_oils':engine_oils}
    return render(request, 'asset/engine-oil/list.html', context=context)

def add_engine_oil(request):

    form = EngineOilCreateForm()
    if request.method == "POST":
        form = EngineOilCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Engine oil added successfully!')
            if request.POST.get('save-list'):
                return redirect('asset:engine_oil_list')
            elif request.POST.get('save-add'):
              return redirect(request.META.get('HTTP_REFERER')) 
        else:
            messages.error(request, form.errors)
    context = {'form':form}
    return render(request, 'asset/engine-oil/create.html', context=context)

def update_engine_oil(request, pk):

    engine_oil = get_object_or_404(EngineOil, id=pk)
    form = EngineOilUpdateForm(instance=engine_oil)
    if request.method == "POST":
        form = EngineOilUpdateForm(request.POST, instance=engine_oil)
        if form.is_valid():
            form.save()
            messages.success(request, f'{engine_oil} updated successfully!')
            return redirect('asset:engine_oil_list')
        else:
            messages.error(request, form.errors)
    context = {'form':form, 'engine_oil':engine_oil}
    return render(request, 'asset/engine-oil/update.html', context=context)