from itertools import product
import uuid
from django.db import models
from common.models import TimeStampModel
from product.models import Product

# Create your models here.

class Asset(TimeStampModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(),editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        abstract = True


class Battery(Asset):
    serial_no = models.CharField(max_length=255, blank=True, null=True)
    model_no = models.CharField(max_length=255, blank=True, null=True)


class EngineOil(Asset):

    SELECT_SIZE = ''
    FIVE_HUNDRED = 500
    EIGHT_HUNDRED = 800
    NINE_HUNDRED = 900
    THOUSAND = 1000

    ENGINE_OIL_CHOICES = (
        ('Select Size', SELECT_SIZE),
        ('500', FIVE_HUNDRED),
        ('800', EIGHT_HUNDRED),
        ('900', NINE_HUNDRED),
        ('1000', THOUSAND)
    )

    size = models.PositiveIntegerField(default=SELECT_SIZE, choices=ENGINE_OIL_CHOICES)
    quantity = models.PositiveIntegerField(blank=True, null=True)


class DistilledWater(Asset):

    SELECT_SIZE = ''
    TWO_AND_HALF = 2.5
    FIVE = 5
    TEN = 10

    DISTILLED_WATER_CHOICES = (
        ('Select Size', SELECT_SIZE),
        ('2.5', TWO_AND_HALF),
        ('5', FIVE),
        ('10', TEN)
    )

    size = models.FloatField(default=SELECT_SIZE, choices=DISTILLED_WATER_CHOICES)
    quantity = models.PositiveIntegerField(blank=True, null=True)
