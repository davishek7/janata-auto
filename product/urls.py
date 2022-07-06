from django.urls  import path
from . import views

app_name = 'product'


urlpatterns = [
    path('list/', views.product_list, name='list'),
    path('add/', views.add_product, name='add'),
    path('update/<uuid:pk>/', views.update_product, name='update'),
    path('add-category/', views.add_product_category, name='add_category'),
]
