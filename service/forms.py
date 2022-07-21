from django import forms
from .models import WarrantyClaim


class WarrantyClaimCreateForm(forms.ModelForm):

    class Meta:
        model = WarrantyClaim


class WarrantyClaimUpdateForm(forms.ModelForm):

    class Meta:
        model = WarrantyClaim