from django import forms
from .fields import GroupedModelChoiceField
from .models import BatterySale, EngineOilSale, DistilledWaterSale, InverterSale, ScrapBatterySale, CustomerDetail
from asset.models import Battery, EngineOil, DistilledWater, Inverter
from vendor.models import Vendor
from .models import jsonfield_default_value


class SaleForm(forms.Form):
    
    date = forms.DateField(required=True, widget=forms.DateInput(
                    attrs={'type':'date','class': 'form-control', 'placeholder':'Date'}))

    price = forms.FloatField(required=True, widget=forms.NumberInput(
                    attrs={'class': 'form-control', 'placeholder':'Price'}))

    discount = forms.FloatField(required=False, widget=forms.NumberInput(
                    attrs={'class': 'form-control', 'placeholder':'Discount'}))


class BatteryInverterCommonForm(forms.Form):
    
    page_number = forms.IntegerField(required=True, widget=forms.NumberInput(
                    attrs={'class': 'form-control', 'placeholder':'Page Number'}))


class BatterySaleForm(forms.ModelForm, SaleForm, BatteryInverterCommonForm):

    battery = GroupedModelChoiceField(queryset=Battery.objects.filter(status=True), 
                required=True, empty_label="Select Battery",
                choices_groupby='product',
                widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta:
        model = BatterySale
        fields = ['battery', 'date', 'price', 'discount', 'page_number']


class BatterySaleUpdateForm(forms.ModelForm, SaleForm, BatteryInverterCommonForm):
    
    class Meta:
        model = BatterySale
        fields = ['date', 'price', 'discount', 'page_number']


class ScrapBatterySaleForm(forms.ModelForm):

    items = forms.JSONField(required=True, widget=forms.Textarea(
                attrs={'class': 'form-control'}))

    date = forms.DateField(required=True, widget=forms.DateInput(
                attrs={'type':'date','class': 'form-control', 'placeholder':'Date'}))
    
    buyer = forms.ModelChoiceField(queryset=Vendor.objects.filter(status=True), 
            required=True, empty_label="Select Buyer", 
            widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = ScrapBatterySale
        fields = ['items', 'date', 'buyer']


class EngineOilSaleForm(forms.ModelForm, SaleForm):

    engine_oil = GroupedModelChoiceField(queryset=EngineOil.objects.filter(status=True, quantity__gt=0), 
                required=True, empty_label="Select Engine Oil",
                choices_groupby='product',
                widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta:
        model = EngineOilSale
        fields = ['engine_oil', 'date', 'price', 'discount']


class DistilledWaterSaleForm(forms.ModelForm, SaleForm):

    distilled_water = GroupedModelChoiceField(queryset=DistilledWater.objects.filter(status=True, quantity__gt=0), 
                required=True, empty_label="Select Distilled Water",
                choices_groupby='product',
                widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta:
        model = DistilledWaterSale
        fields = ['distilled_water', 'date', 'price', 'discount']


class CustomerDetailForm(forms.ModelForm):

    name = forms.CharField(required=False, widget=forms.TextInput(
                    attrs={'class': 'form-control', 'placeholder':'Customer Name'}))

    phone = forms.IntegerField(required=False, widget=forms.NumberInput(
                    attrs={'class': 'form-control', 'placeholder':'Customer Phone'}))

    class Meta:
        model = CustomerDetail
        fields = ['name', 'phone']