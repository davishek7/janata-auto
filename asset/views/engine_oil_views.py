from django.shortcuts import render
from ..forms import EngineOilCreateForm


def engine_oil_list(request):
    return render(request, 'asset/engine-oil/list.html')

def add_engine_oil(request):
    form = EngineOilCreateForm()
    context = {'form':form}
    return render(request, 'asset/engine-oil/create.html', context=context)