from django import forms
from .models import BatteryWarrantyClaim


class WarrantyClaimCreateForm(forms.ModelForm):

    serial_no = forms.CharField(required=True, widget=forms.TextInput(
                    attrs={'class': 'form-control', 'placeholder':'Serial No'}))

    claim_status = forms.CharField(required=True, widget=forms.Select(choices=BatteryWarrantyClaim.STATUS_CHOICES,
                    attrs={'class': 'form-control', 'placeholder':'Claim Status'}))

    purchase_date = forms.DateField(required=True, widget=forms.DateInput(
                    attrs={'type':'date','class': 'form-control', 'placeholder':'Purchase Date'}))

    receive_date = forms.DateField(required=False, widget=forms.DateInput(
                    attrs={'type':'date','class': 'form-control', 'placeholder':'Receive Date'}))

    send_date = forms.DateField(required=False, widget=forms.DateInput(
                    attrs={'type':'date','class': 'form-control', 'placeholder':'Send Date'}))

    return_date = forms.DateField(required=False, widget=forms.DateInput(
                    attrs={'type':'date','class': 'form-control', 'placeholder':'Return Date'}))

    handover_date = forms.DateField(required=False, widget=forms.DateInput(
                    attrs={'type':'date','class': 'form-control', 'placeholder':'Handover Date'}))

    new_serial_no = forms.CharField(required=False, widget=forms.TextInput(
                    attrs={'class': 'form-control', 'placeholder':'New Serial No'}))

    transport = forms.CharField(required=False, widget=forms.Select(choices=BatteryWarrantyClaim.TRANSPORT_CHOICES,
                    attrs={'class': 'form-control', 'placeholder':'Transport'}))

    claim_success = forms.BooleanField(required=True, widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))

    class Meta:
        model = BatteryWarrantyClaim
        fields = ['serial_no', 'claim_status', 'purchase_date', 'receive_date', 'send_date', 'return_date', 'handover_date', 'new_serial_no', 'transport', 'claim_success']