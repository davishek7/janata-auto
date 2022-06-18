from django.urls  import path
from . import views

app_name = 'asset'


urlpatterns = [
    path('list', views.asset_list, name='list'),
]