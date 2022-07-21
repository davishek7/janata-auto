from ast import In
from django.contrib import admin
from .models import Battery, DistilledWater, Inverter, EngineOil

# Register your models here.

admin.site.register(Battery)
admin.site.register(EngineOil)
admin.site.register(Inverter)
admin.site.register(DistilledWater)