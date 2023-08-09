from django.shortcuts import render
from django.db.models import Q
from .forms import SearchForm
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

        products = Product.objects.filter(Q(name__icontains=search_term) |
                                          Q(size__size__icontains=search_term) |
                                          Q(model_no__icontains=search_term) |
                                          Q(mrp__icontains=search_term) |
                                          Q(selling_price__icontains=search_term) |
                                          Q(category__name__icontains=search_term) |
                                          Q(vendor__name__icontains=search_term)).filter(status=True).all()

        vendors = Vendor.objects.filter(Q(name__icontains=search_term) |
                                        Q(phone__icontains=search_term) |
                                        Q(email__icontains=search_term)).filter(status=True).all()

        batteries = Battery.objects.filter(Q(product__name__icontains=search_term) |
                                           Q(serial_no__icontains=search_term)).filter(status=True).all()

        engine_oils = EngineOil.objects.filter(Q(product__name__icontains=search_term) |
                                               Q(quantity__icontains=search_term)).filter(status=True).all()

        distilled_waters = DistilledWater.objects.filter(Q(product__name__icontains=search_term) |
                                                         Q(quantity__icontains=search_term)).filter(status=True).all()

        inverters = Inverter.objects.filter(Q(product__name__icontains=search_term) |
                                            Q(serial_no__icontains=search_term)).filter(status=True).all()

        claims = BatteryWarrantyClaim.objects.filter(Q(claim_status__icontains=search_term) |
                                                     Q(serial_no__icontains=search_term) |
                                                     Q(new_serial_no__icontains=search_term) |
                                                     Q(transport__icontains=search_term) |
                                                     Q(customer__name__icontains=search_term) |
                                                     Q(customer__phone__icontains=search_term) |
                                                     Q(claim_success__icontains=search_term)).filter(status=True).all()

        battery_sale = BatterySale.objects.filter(Q(battery__product__name__icontains=search_term) |
                                                  Q(battery__serial_no__icontains=search_term) |
                                                  Q(price__icontains=search_term) |
                                                  Q(discount__icontains=search_term) |
                                                  Q(date__icontains=search_term) |
                                                  Q(page_number__icontains=search_term) |
                                                  Q(customer__name__icontains=search_term) |
                                                  Q(customer__phone__icontains=search_term)).filter(status=True).all()

        eo_sale = EngineOilSale.objects.filter(Q(engine_oil__product__name__icontains=search_term) |
                                               Q(engine_oil__product__size__size__icontains=search_term) |
                                               Q(price__icontains=search_term) |
                                               Q(discount__icontains=search_term) |
                                               Q(date__icontains=search_term)).filter(status=True).all()

        dw_sale = DistilledWaterSale.objects.filter(Q(distilled_water__product__name__icontains=search_term) |
                                                    Q(distilled_water__product__size__size__icontains=search_term) |
                                                    Q(price__icontains=search_term) |
                                                    Q(discount__icontains=search_term) |
                                                    Q(date__icontains=search_term)).filter(status=True).all()

        inverter_sale = InverterSale.objects.filter(Q(inverter__product__name__icontains=search_term) |
                                                    Q(inverter__serial_no__icontains=search_term) |
                                                    Q(price__icontains=search_term) |
                                                    Q(discount__icontains=search_term) |
                                                    Q(date__icontains=search_term) |
                                                    Q(page_number__icontains=search_term) |
                                                    Q(customer__name__icontains=search_term) |
                                                    Q(customer__phone__icontains=search_term)).filter(status=True).all()

        scrap_battery_sale = ScrapBatterySale.objects.filter(Q(date__icontains=search_term) |
                                                             Q(buyer__name__icontains=search_term)).filter(status=True).all()

        total_count = (products.count() + vendors.count() + batteries.count() + engine_oils.count() + distilled_waters.count() + inverters.count() +
                       claims.count() + battery_sale.count() + eo_sale.count() + dw_sale.count() + scrap_battery_sale.count() + inverter_sale.count())

    context = {
        'products': products, 'vendors': vendors, 'batteries': batteries, 'engine_oils': engine_oils, 'distilled_waters': distilled_waters,
        'inverters': inverters, 'claims': claims, 'battery_sales': battery_sale, 'eo_sale': eo_sale, 'dw_sale': dw_sale, 'scrap_battery_sale': scrap_battery_sale,
        'inverter_sale': inverter_sale, 'total_count': total_count
    }

    return render(request, 'search/list.html', context=context)
