from django.urls import path
from . import views

app_name = 'authentication'


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    # path('earnings-chart/', views.earnings_chart, name='earnings_chart'),
]
