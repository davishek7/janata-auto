from django import forms
from .models import Address

class AddressForm(forms.ModelForm):

    address_line_one = forms.CharField(required=True, widget=forms.Textarea(
                    attrs={'class': 'form-control', 'placeholder':'Address Line 1'}))

    address_line_two = forms.CharField(required=True, widget=forms.Textarea(
                    attrs={'class': 'form-control', 'placeholder':'Address Line 2'}))

    district = forms.CharField(required=True, widget=forms.TextInput(
                    attrs={'class': 'form-control', 'placeholder':'District'}))

    state = forms.CharField(required=True, widget=forms.TextInput(
                    attrs={'class': 'form-control', 'placeholder':'State'}))

    country = forms.CharField(required=True, widget=forms.TextInput(
                    attrs={'class': 'form-control', 'placeholder':'Country'}))

    class Meta:
        model = Address
        fields = ['address_line_one', 'address_line_two', 'district', 'state', 'country']


class SearchForm(forms.Form):

    q = forms.CharField(label='', required=True, widget=forms.TextInput(
            attrs={'class':'form-control bg-light border-0 small', 'placeholder':'Search for...'}))