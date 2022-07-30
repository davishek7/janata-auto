from django import forms
from .models import Sale, CustomerDetail
from product.models import ProductCategory

class SaleForm(forms.ModelForm):

    category = forms.ModelChoiceField(queryset=ProductCategory.objects.all(), 
                required=True, empty_label="Select Category", 
                widget=forms.Select(attrs={'class': 'form-control'}))

    serial_no = forms.CharField(required=False, widget=forms.TextInput(
                    attrs={'class': 'form-control', 'placeholder':'Serial No'}))

    date = forms.DateField(required=True, widget=forms.DateInput(
                    attrs={'type':'date','class': 'form-control', 'placeholder':'Date'}))

    price = forms.FloatField(required=True, widget=forms.NumberInput(
                    attrs={'class': 'form-control', 'placeholder':'Price'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['product'].widget.attrs.update({
            'class':'form-control'
        })
    
    class Meta:
        model = Sale
        fields = ['category', 'product', 'serial_no', 'date', 'price']


class CustomerDetailForm(forms.ModelForm):

    customer_name = forms.CharField(required=False, widget=forms.TextInput(
                    attrs={'class': 'form-control', 'placeholder':'Customer Name'}))

    customer_phone = forms.IntegerField(required=False, widget=forms.NumberInput(
                    attrs={'class': 'form-control', 'placeholder':'Customer Phone'}))

    class Meta:
        model = CustomerDetail
        fields = ['customer_name', 'customer_phone']