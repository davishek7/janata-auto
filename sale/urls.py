from django.urls  import path
from . import views

app_name = 'sale'


urlpatterns = [
    # Battery sale urls
    path('battery/list/', views.battery_sale_list, name='battery_sale_list'),
    path('battery/add/', views.add_battery_sale, name='add_battery_sale'),
    path('battery/update/<uuid:pk>/', views.update_battery_sale, name='update_battery_sale'),

    # Inverter sale urls
    # path('inverter/list/', views.inverter_list, name='inverter_list'),
    # path('inverter/add/', views.add_inverter, name='add_inverter'),
    # path('inverter/update/<uuid:pk>/', views.update_inverter, name='update_inverter'),

    # Engine oil sale urls
    path('engine-oil/list/', views.engine_oil_sale_list, name='engine_oil_sale_list'),
    path('engine-oil/add/', views.add_engine_oil_sale, name='add_engine_oil_sale'),
    path('engine-oil/update/<uuid:pk>/', views.update_engine_oil_sale, name='update_engine_oil_sale'),

    # Distilled water sale urls
    path('distilled-water/list/', views.distilled_water_sale_list, name='distilled_water_sale_list'),
    path('distilled-water/add/', views.add_distilled_water_sale, name='add_distilled_water_sale'),
    path('distilled-water/update/<uuid:pk>/', views.update_distilled_water_sale, name='update_distilled_water_sale'),

    # Scrap battery sale urls
    path('scrap-battery/list/', views.scrap_battery_sale_list, name='scrap_battery_sale_list'),
    path('scrap-battery/add/', views.add_scrap_battery_sale, name='add_scrap_battery_sale'),
    path('scrap-battery/update/<uuid:pk>/', views.update_scrap_battery_sale, name='update_scrap_battery_sale'),
]