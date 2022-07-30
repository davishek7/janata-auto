from django import forms
from .models import VendorTransaction
from vendor.models import Vendor


class VendorTransactionForm(forms.ModelForm):

    type = forms.CharField(required=True, widget=forms.Select(choices=VendorTransaction.TYPE_CHOICES,
                    attrs={'class': 'form-control', 'placeholder':'Transaction Type'}))

    date = forms.DateField(required=False, widget=forms.DateInput(
                    attrs={'type':'date','class': 'form-control', 'placeholder':'Transaction Date'}))

    amount = forms.FloatField(required=True, widget=forms.NumberInput(
                    attrs={'class': 'form-control', 'placeholder':'Transaction Amount'}))

    description = forms.CharField(required=True, widget=forms.Textarea(
                    attrs={'class': 'form-control', 'placeholder':'Description', 'rows':2}))

    class Meta:
        model = VendorTransaction
        fields = ['type', 'amount', 'date', 'description']