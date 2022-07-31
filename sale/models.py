import uuid
from django.db import models
from common.models import TimeStampModel, Address
from product.models import ProductCategory, Product
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.

class Sale(TimeStampModel):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(ProductCategory, on_delete=models.DO_NOTHING, blank=True, null=True)
    product = ChainedForeignKey(Product, chained_field="category", chained_model_field="category", show_all=False, auto_choose=True, sort=True, null=True, blank=True)
    serial_no = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True, default=0)
    customer = models.ForeignKey('CustomerDetail', on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return f'{self.category} - {self.product} - {self.date} - {self.price}'

    @property
    def get_net_price(self):
        return (self.price - self.discount)


class CustomerDetail(TimeStampModel):
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    customer_phone = models.CharField(max_length=255, blank=True, null=True)
    customer_address = models.OneToOneField(Address, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.customer_name}'s details"