import uuid
from django.db import models
from common.models import TimeStampModel
from sale.models import Sale

# Create your models here.

class WarrantyClaim(TimeStampModel):

    SELECT_STATUS = ''
    RECEIVED = 'Received'
    SEND_TO_COMPANY = 'Send to Company'
    RETURNED_OK = 'Returned OK'
    FOC = 'F.O.C.'
    HANDOVER_TO_CUSTOMER = 'Handover to Customer'

    SELECT_TRANSPORT = ''
    DEALER_VEHICLE = 'Dealer Vehicle'
    BUS = 'Bus'

    STATUS_CHOICES = (
        ('Select Status', SELECT_STATUS),
        ('Received', RECEIVED),
        ('Send to Company', SEND_TO_COMPANY),
        ('Returned_OK', RETURNED_OK),
        ('F.O.C.', FOC),
        ('Handover to Customer', HANDOVER_TO_CUSTOMER)
        )

    TRANSPORT_CHOICES = (        
        ('Select Transport', SELECT_TRANSPORT),
        ('Dealer Vehicle', DEALER_VEHICLE),
        ('Bus', BUS),
        )
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    claim_status = models.CharField(max_length=50, choices=STATUS_CHOICES, blank=True, null=True)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    transport = models.CharField(max_length=50, choices=TRANSPORT_CHOICES, blank=True, null=True)