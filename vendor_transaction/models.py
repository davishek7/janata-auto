import uuid
from django.db import models
from common.models import TimeStampModel
from vendor.models import Vendor

# Create your models here.

class VendorTransaction(TimeStampModel):

    SELECT_TYPE = ''
    PURCHASE = 'Purchase'
    PAYMENT = 'Payment'

    TYPE_CHOICES = (
        (SELECT_TYPE, 'Select Transaction Type'),
        (PURCHASE, 'Purchase'),
        (PAYMENT, 'Payment'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return f"{self.vendor} - {self.date} - {self.amount} - {self.type}"
