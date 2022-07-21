from django.shortcuts import render
from vendor.models import Vendor
from product.models import Product
from asset.models import Battery, EngineOil, DistilledWater

# Create your views here.

def index(request):
    vendor_count = Vendor.objects.filter(status=True).count()
    product_count = Product.objects.filter(status=True).count()
    battery_count = Battery.objects.filter(status=True).count()
    eo_count = EngineOil.total_quantity() if EngineOil.total_quantity() is not None else 0
    dw_count = DistilledWater.total_quantity() if DistilledWater.total_quantity() is not None else 0
    asset_count = (battery_count + eo_count + dw_count)
    context = {'vendor_count':vendor_count, 'product_count':product_count, 'asset_count':asset_count}
    return render(request, 'auth/index.html', context=context)
