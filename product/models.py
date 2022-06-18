import uuid
from django.db import models
from common.models import TimeStampModel
from vendor.models import Vendor

# Create your models here.

class ProductCategory(TimeStampModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=255, blank=True, null=True)


class Product(TimeStampModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=255, blank=True, null=True)
    mrp_price = models.FloatField(blank=True, null=True)
    selling_price = models.FloatField(blank=True, null=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, blank=True, null=True)