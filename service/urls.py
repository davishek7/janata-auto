from django.urls import path
from . import views

app_name = 'service'


urlpatterns = [

    path('list/', views.claims_list, name='list'),
    path('add/', views.add_claim, name='add'),
    path('update/<uuid:pk>/', views.update_claim, name='update'),
    
]