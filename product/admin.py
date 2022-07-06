from django.contrib import admin
from .models import Product, ProductSize, ProductCategory

# Register your models here.

admin.site.register(ProductCategory)
admin.site.register(ProductSize)