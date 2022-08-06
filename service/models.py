import uuid
from django.db import models
from django.dispatch import receiver
from common.models import TimeStampModel
from sale.models import CustomerDetail

# Create your models here.

class BatteryWarrantyClaim(TimeStampModel):

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
        (SELECT_STATUS, 'Select Status'),
        (RECEIVED, 'Received'),
        (SEND_TO_COMPANY,'Send to Company'),
        (RETURNED_OK,'Returned_OK'),
        (FOC,'F.O.C.'),
        (HANDOVER_TO_CUSTOMER,'Handover to Customer')
        )

    TRANSPORT_CHOICES = (        
        (SELECT_TRANSPORT,'Select Transport'),
        (DEALER_VEHICLE,'Dealer Vehicle'),
        (BUS,'Bus'),
        )
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    claim_status = models.CharField(max_length=50, choices=STATUS_CHOICES, blank=True, null=True)
    serial_no = models.CharField(max_length=50, blank=True, null=True)
    purchase_date = models.DateField(blank=True, null=True)
    receive_date = models.DateField(blank=True, null=True)
    send_date = models.DateField(blank=True, null=True)
    return_date = models.DateField(blank=True, null=True)
    handover_date = models.DateField(blank=True, null=True)
    new_serial_no = models.CharField(max_length=50, blank=True, null=True)
    transport = models.CharField(max_length=50, choices=TRANSPORT_CHOICES, blank=True, null=True)
    customer = models.OneToOneField(CustomerDetail, on_delete=models.DO_NOTHING, blank=True, null=True)