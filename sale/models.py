import uuid
from datetime import datetime
from django.db import models
from django.db.models import Sum
from common.models import TimeStampModel, Address
from vendor.models import Vendor
from asset.models import Battery, Inverter, EngineOil, DistilledWater

# Create your models here.

def jsonfield_default_value():
    return [{"item":"TZ4", "quantity":0, "price_per_piece":120}]

def get_now():
    return datetime.now()

class Sale(TimeStampModel):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True, default=0)

    @property
    def get_net_price(self):
        return self.price - self.discount

    @classmethod
    def get_monthly_sale(cls):
        total_sale = 0
        for sale in cls.objects.filter(status = True, date__month = get_now().month):
            total_sale += sale.get_net_price
        return total_sale

    @classmethod
    def get_yearly_sale(cls):
        total_sale = 0
        for sale in cls.objects.filter(status = True, date__year = get_now().year):
            total_sale += sale.get_net_price
        return total_sale

    class Meta:
        abstract = True
        ordering = ['-date']


class BICommonFields(Sale):

    customer = models.ForeignKey('CustomerDetail', on_delete=models.DO_NOTHING, blank=True, null=True)
    page_number = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        abstract = True


class BatterySale(BICommonFields):

    battery = models.ForeignKey(Battery, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return f'{self.battery} sale'


class EngineOilSale(Sale):

    engine_oil = models.ForeignKey(EngineOil, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return f'{self.engine_oil} sale'


class DistilledWaterSale(Sale):

    distilled_water = models.ForeignKey(DistilledWater, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return f'{self.distilled_water} sale'


class InverterSale(BICommonFields):

    inverter = models.ForeignKey(Inverter, on_delete=models.DO_NOTHING, blank=True, null=True)
    
    def __str__(self):
        return f'{self.inverter} sale'


class ScrapBatterySale(TimeStampModel):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    items = models.JSONField(default=jsonfield_default_value)
    date = models.DateField(blank=True, null=True)
    buyer = models.ForeignKey(Vendor, on_delete=models.DO_NOTHING, blank=True, null=True)

    @property
    def get_total_price(self):
        total_price = 0
        for _ in range(len(self.items)):
            total_price += (self.items[_]['quantity'] * self.items[_]['price_per_piece'])
        return total_price

    @property
    def get_formatted_data(self):
        data = ''
        for _ in range(len(self.items)):
            data += (self.items[_]['item'] + ' : ' + str(self.items[_]['quantity']) + ' X ' + str(self.items[_]['price_per_piece']) + ' | ' )
        return data

    @classmethod
    def get_monthly_sale(cls):
        total_sale = 0
        for sale in cls.objects.filter(status = True, date__month = get_now().month):
            total_sale += sale.get_total_price
        return total_sale

    @classmethod
    def get_yearly_sale(cls):
        total_sale = 0
        for sale in cls.objects.filter(status = True, date__year = get_now().year):
            total_sale += sale.get_total_price
        return total_sale

    def __str__(self):
        return f'Scrap batteries sold to {self.buyer} on {self.date}'


class CustomerDetail(TimeStampModel):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name