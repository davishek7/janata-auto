from django.urls  import path
from . import views

app_name = 'trash'


urlpatterns = [
    path('vendors/', views.deleted_vendors, name='vendors'),
    path('restore/vendor/<uuid:pk>/', views.restore_vendor, name='restore_vendor'),

    path('products/', views.deleted_products, name='products'),
    path('restore/product/<uuid:pk>/', views.restore_product, name='restore_product'),
]