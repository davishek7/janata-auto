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

    DEALER_VEHICLE = 'Dealer Vehicle'
    BUS = 'Bus'

    STATUS_CHOICES = (
        ('Select Status', SELECT_STATUS),
        ('Received', RECEIVED),
        ('Send to Company', SEND_TO_COMPANY),
        ('Returned_OK', RETURNED_OK),
        ('F.O.C.', FOC)
        )

    TRANSPORT_CHOICES = (        
        ('Select Status', SELECT_STATUS),
        ('Dealer Vehicle', DEALER_VEHICLE),
        ('Bus', BUS),
        )
    
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, blank=True, null=True)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    received_date = models.DateField(blank=True, null=True)
    send_date = models.DateField(blank=True, null=True)
    return_date = models.DateField(blank=True, null=True)
    handover_date = models.DateField(blank=True, null=True)
    transport = models.CharField(max_length=50, choices=TRANSPORT_CHOICES, blank=True, null=True)