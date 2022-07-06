from itertools import product
import uuid
from django.db import models
from django.db.models import Sum
from common.models import TimeStampModel
from product.models import Product

# Create your models here.

class Asset(TimeStampModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='asset_images', blank=True, null=True)

    class Meta:
        abstract = True


class Battery(Asset):
    serial_no = models.CharField(max_length=255, blank=True, null=True)
    model_no = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.serial_no
    

class EngineOil(Asset):

    model_no = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.product}-{self.size} ml'
    
    @classmethod
    def total_quantity(self):
        return self.objects.all().aggregate(total_quantity=Sum('quantity')).get('quantity',0)


class DistilledWater(Asset):

    quantity = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.product}-{self.size} l'

    @classmethod
    def total_quantity(self):
        return self.objects.all().aggregate(total_quantity=Sum('quantity')).get('quantity',0)