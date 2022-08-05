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
            (SELECT_TYPE, 'Select Type'),
            (SUCCESS, 'Success'),
            (WARNING, 'Warning'),
            (INFO, 'Info'),
            (ERROR, 'Error')
        )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=255, choices=TYPE_CHOICES, blank=True, null=True)
    read_status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} - {self.type} - {self.read_status}'
