import uuid
from django.db import models
from common.models import TimeStampModel
from vendor.models import Vendor
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.

class ProductCategory(TimeStampModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'product categories'
        

class ProductSize(TimeStampModel):

    SELECT_SIZE = ''
    FIVE_HUNDRED = 500
    EIGHT_HUNDRED = 800
    NINE_HUNDRED = 900
    THOUSAND = 1000
    TWO = 2
    FIVE = 5
    TEN = 10

    PRODUCT_SIZE_CHOICES = (
        (SELECT_SIZE, 'Select Size'),
        (FIVE_HUNDRED, 500),
        (EIGHT_HUNDRED, 800),
        (NINE_HUNDRED, 900),
        (THOUSAND, 1000),
        (TWO, 2),
        (FIVE, 5),
        (TEN, 10)
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    size = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.size
        

class Product(TimeStampModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=True, null=True)
    mrp = models.FloatField(blank=True, null=True)
    selling_price = models.FloatField(blank=True, null=True)
    image = models.ImageField(upload_to='product_images', blank=True, null=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    size = ChainedForeignKey(ProductSize, chained_field="category", chained_model_field="category", show_all=False, auto_choose=True, sort=True, null=True, blank=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.size}' if self.size else self.name