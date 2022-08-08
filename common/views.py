from django.shortcuts import render
from django.db.models import Q
from .forms import SearchForm
from django.http import JsonResponse
from asset.models import Battery, DistilledWater, EngineOil, Inverter
from sale.models import BatterySale, EngineOilSale, DistilledWaterSale, ScrapBatterySale, InverterSale
from service.models import BatteryWarrantyClaim
from product.models import Product
from vendor.models import Vendor

# Create your views here.

def search(request):

    search_form = SearchForm(request.GET)
    if search_form.is_valid():
        search_term = search_form.cleaned_data.get('q')

        products = Product.objects.filter(Q(name__icontains = search_term)|Q(size__size__icontains=search_term)).all()