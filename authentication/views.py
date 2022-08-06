from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum
from vendor.models import Vendor
from product.models import Product
from asset.models import Battery, EngineOil, DistilledWater, Inverter
from sale.models import BatterySale, EngineOilSale, DistilledWaterSale, ScrapBatterySale, InverterSale

# Create your views here.

def index(request):

    vendor_count = Vendor.objects.filter(status=True).count()
    product_count = Product.objects.filter(status=True).count()

    battery_count = Battery.objects.filter(status=True).count()
    eo_count = EngineOil.total_quantity() if EngineOil.total_quantity() is not None else 0
    dw_count = DistilledWater.total_quantity() if DistilledWater.total_quantity() is not None else 0
    inverter_count = Inverter.objects.filter(status=True).count()
    asset_count = (battery_count + eo_count + dw_count + inverter_count)

    monthly_battery_sale = BatterySale.get_monthly_sale()
    monthly_engine_oil_sale = EngineOilSale.get_monthly_sale()
    monthly_dw_sale = DistilledWaterSale.get_monthly_sale()
    monthly_inverter_sale = InverterSale.get_monthly_sale()
    monthly_scrap_battery_sale = ScrapBatterySale.get_monthly_sale()

    total_monthly_sale = monthly_battery_sale + monthly_engine_oil_sale + monthly_dw_sale + monthly_scrap_battery_sale + monthly_inverter_sale

    yearly_battery_sale = BatterySale.get_yearly_sale()
    yearly_engine_oil_sale = EngineOilSale.get_yearly_sale()
    yearly_dw_sale = DistilledWaterSale.get_yearly_sale()
    yearly_inverter_sale = InverterSale.get_yearly_sale()
    yearly_scrap_battery_sale = ScrapBatterySale.get_yearly_sale()

    total_yearly_sale = yearly_battery_sale + yearly_engine_oil_sale + yearly_dw_sale + yearly_scrap_battery_sale + yearly_inverter_sale

    context = {
                'vendor_count':vendor_count, 'product_count':product_count, 'asset_count':asset_count, 
                'sidebar':'home', 'total_monthly_sale':total_monthly_sale, 'total_yearly_sale':total_yearly_sale,
            }
    return render(request, 'auth/index.html', context=context)

def login(request):
    return render(request, 'auth/login.html')

# def earnings_chart(request):
#     labels = []
#     data = []

#     queryset = BatterySale.objects.values('date__month').annotate(country_population=Sum('population')).order_by('-country_population')
#     for entry in queryset:
#         labels.append(entry['country__name'])
#         data.append(entry['country_population'])
    
#     return JsonResponse(data={
#         'labels': labels,
#         'data': data,
#     })
