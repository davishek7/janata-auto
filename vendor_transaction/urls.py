from django.urls import path
from . import views

app_name = 'transaction'


urlpatterns = [
    path('list/<uuid:vendor_id>/', views.transactions_list, name='list'),
    path('create/<uuid:vendor_id>/', views.make_transaction, name='create'),
]