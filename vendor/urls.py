from django.urls import path
from . import views

app_name = 'vendor'


urlpatterns = [
    path('list', views.vendor_list, name='list')
]
