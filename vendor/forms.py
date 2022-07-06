from django import forms
from .models import Vendor


class VendorForm(forms.ModelForm):

    name = forms.CharField(required=True, widget=forms.TextInput(
                    attrs={'class': 'form-control', 'row':"2", 'placeholder':'Name'}))

    phone = forms.IntegerField(required=True, widget=forms.NumberInput(
                    attrs={'class': 'form-control', 'row':"2", 'placeholder':'Phone'}))

    email = forms.EmailField(required=False, widget=forms.EmailInput(
                    attrs={'class': 'form-control', 'placeholder':'Email'}))

    class Meta:
        model = Vendor
        fields = ['name', 'phone', 'email']