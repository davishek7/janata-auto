from django.urls  import path
from . import views

app_name = 'asset'


urlpatterns = [

    # Battery urls
    path('battery/list/', views.battery_list, name='battery_list'),
    path('battery/add/', views.add_battery, name='add_battery'),

    # Inverter urls
    

    # Engine oil urls
    path('engine-oil/list/', views.engine_oil_list, name='engine_oil_list'),
    path('engine-oil/add/', views.add_engine_oil, name='add_engine_oil'),

    # Distilled water urls
]