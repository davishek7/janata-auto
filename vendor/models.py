import uuid
from django.db import models
from authentication.models import TimeStampModel

# Create your models here.

class Vendor(TimeStampModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    address = models.ForeignKey('Address', on_delete=models.CASCADE)

    def __repr__(self):
        return '<Vendor {self.name}>'
    


class Address(TimeStampModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    address_line_one = models.CharField(max_length=255, blank=True, null=True)
    address_line_two = models.CharField(max_length=255, blank=True, null=True)
    district = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    pin_code = models.CharField(max_length=255, blank=True, null=True)

    def __repr__(self):
        return '<Address {}>'