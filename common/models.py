import uuid
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.

class TimeStampModel(models.Model):
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Address(TimeStampModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    address_line_one = models.CharField(max_length=255, blank=True, null=True)
    address_line_two = models.CharField(max_length=255, blank=True, null=True)
    district = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    pin_code = models.CharField(max_length=255, blank=True, null=True)

    def __repr__(self):
        return '<Address {self.address_line_one}, {self.address_line_two}, {self.district}, {self.state}, {self.country}, {self.pin_code}>'


class Image(TimeStampModel):
    name = models.ImageField(blank=True, null=True)
    limit = models.Q(
                    app_label = 'vendor', model = 'Vendor') | models.Q(
                    app_label = 'product', model = 'Product') | models.Q(
                    app_label = 'asset', model = 'Asset'
                    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to = limit)
    object_id = models.UUIDField()
    content_object = GenericForeignKey('content_type', 'object_id')