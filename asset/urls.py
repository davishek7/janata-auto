from django.urls  import path
from . import views

app_name = 'asset'


urlpatterns = [

    # Battery urls
    path('battery/list/', views.battery_list, name='battery_list'),
    path('battery/add/', views.add_battery, name='add_battery'),
    path('battery/update/<uuid:pk>/', views.update_battery, name='update_battery'),

    # Inverter urls
    # path('inverter/list/', views.inverter_list, name='inverter_list'),
    # path('inverter/add/', views.add_inverter, name='add_inverter'),
    # path('inverter/update/<uuid:pk>/', views.update_inverter, name='update_inverter'),

    # Engine oil urls
    path('engine-oil/list/', views.engine_oil_list, name='engine_oil_list'),
    path('engine-oil/add/', views.add_engine_oil, name='add_engine_oil'),
    path('engine-oil/update/<uuid:pk>/', views.update_engine_oil, name='update_engine_oil'),

    # Distilled water urls
    path('distilled-water/list/', views.distilled_water_list, name='distilled_water_list'),
    path('distilled-water/add/', views.add_distilled_water, name='add_distilled_water'),
    path('distilled-water/update/<uuid:pk>/', views.update_distilled_water, name='update_distilled_water'),

]