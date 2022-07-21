from django.urls import path
from . import views

app_name = 'vendor'


urlpatterns = [
    path('list/', views.vendor_list, name='list'),
    path('add/', views.add_vendor, name='add'),
    path('update/<uuid:pk>/', views.update_vendor, name='update'),
    path('delete/<uuid:pk>/', views.delete_vendor, name='delete')
]
