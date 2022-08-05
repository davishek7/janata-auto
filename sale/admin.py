from django.contrib import admin
from .models import BatterySale, EngineOilSale, DistilledWaterSale, InverterSale, ScrapBatterySale, CustomerDetail

# Register your models here.

admin.site.register(BatterySale)
admin.site.register(EngineOilSale)
admin.site.register(DistilledWaterSale)
admin.site.register(ScrapBatterySale)
admin.site.register(InverterSale)
admin.site.register(CustomerDetail)