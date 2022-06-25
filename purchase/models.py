import uuid
from django.db import models
from common.models import TimeStampModel

# Create your models here.

class Purchase(TimeStampModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)