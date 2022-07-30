from django.urls  import path
from . import views

app_name = 'sale'


urlpatterns = [
    path('list/', views.sale_list, name='list'),
    path('create/', views.add_sale, name='create'),
]