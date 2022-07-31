import uuid
from django.db import models

# Create your models here.

class TimeStampModel(models.Model):
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']


class Address(TimeStampModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    address_line_one = models.CharField(max_length=255, blank=True, null=True)
    address_line_two = models.CharField(max_length=255, blank=True, null=True)
    district = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return f'{self.address_line_one}, {self.address_line_two}, {self.district}, {self.state}, {self.country}'