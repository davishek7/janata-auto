from django.shortcuts import render
from vendor.models import Vendor
from product.models import Product
from asset.models import Battery, EngineOil, DistilledWater

# Create your views here.

def index(request):
    vendor_count = Vendor.objects.filter(status=True).count()
    product_count = Product.objects.filter(status=True).count()
    battery_count = Battery.objects.filter(status=True).count()
    eo_count = EngineOil.total_quantity()
    dw_count = DistilledWater.total_quantity()
    asset_count = (battery_count + eo_count + dw_count)
    context = {'vendor_count':vendor_count, 'product_count':product_count, 'asset_count':asset_count}
    return render(request, 'auth/index.html', context=context)
