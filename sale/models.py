import uuid
from django.db import models
from common.models import TimeStampModel, Address

# Create your models here.

class Sale(TimeStampModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class SaleItem(TimeStampModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, blank=True, null=True)