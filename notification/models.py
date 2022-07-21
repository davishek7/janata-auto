from logging import WARNING
import uuid
from django.db import models
from common.models import TimeStampModel

# Create your models here.

class Notification(TimeStampModel):

    SELECT_TYPE = ''
    SUCCESS = 'success'
    WARNING = 'warning'
    INFO = 'info'
    ERROR = 'error'

    TYPE_CHOICES = (
            ('Select Type', SELECT_TYPE),
            ('Success', SUCCESS),
            ('Warning',WARNING),
            ('Info', INFO),
            ('Error', ERROR)
        )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=255, choices=TYPE_CHOICES, blank=True, null=True)
