from django.urls import path
from . import views

app_name = 'product'


urlpatterns = [
    path('list/', views.product_list, name='list'),
    path('add/', views.add_product, name='add'),
    path('update/<uuid:pk>/', views.update_product, name='update'),
    path('add-category/', views.add_product_category, name='add_product_category'),
    path('list-category/', views.list_product_category, name='list_product_category'),
    path('update-category/<uuid:pk>', views.update_product_category, name='update_product_category'),
    path('add-size/', views.add_product_size, name='add_product_size'),
    path('list-size/', views.list_product_size, name='list_product_size'),
    path('update-size/<uuid:pk>', views.update_product_size, name='update_product_size'),
]
