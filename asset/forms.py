from django import forms
from product.models import Product
from .models import Battery, EngineOil, DistilledWater, Inverter


class BatteryCreateForm(forms.ModelForm):

    product = forms.ModelChoiceField(queryset=Product.objects.filter(category__name='Battery'), 
                required=True, empty_label="Select Product", 
                widget=forms.Select(attrs={'class': 'form-control'}))

    serial_no = forms.CharField(required=True, widget=forms.TextInput(
                attrs={'class': 'form-control', 'placeholder':'Serial No'}))

    def clean_serial_no(self):
        serial_no = self.cleaned_data.get('serial_no')
        if '/' not in serial_no:
            raise forms.ValidationError("'/' must be in serial no")
        return serial_no

    class Meta:
        model = Battery
        fields = ['product', 'serial_no']


class BatteryUpdateForm(forms.ModelForm):

    serial_no = forms.CharField(required=True, widget=forms.TextInput(
                attrs={'class': 'form-control', 'placeholder':'Serial No'}))

    def clean_serial_no(self):
        serial_no = self.cleaned_data.get('serial_no')
        if '/' not in serial_no:
            raise forms.ValidationError("'/' must be in serial no")
        return serial_no

    class Meta:
        model = Battery
        fields = ['serial_no']


class InverterCreateForm(forms.ModelForm):

    product = forms.ModelChoiceField(queryset=Product.objects.filter(category__name='Battery'), 
                required=True, empty_label="Select Product", 
                widget=forms.Select(attrs={'class': 'form-control'}))

    serial_no = forms.CharField(required=True, widget=forms.TextInput(
                attrs={'class': 'form-control', 'placeholder':'Serial No'}))

    class Meta:
        model = Inverter
        fields = ['product', 'serial_no']


class InverterUpdateForm(forms.ModelForm):

    serial_no = forms.CharField(required=True, widget=forms.TextInput(
                attrs={'class': 'form-control', 'placeholder':'Serial No'}))

    class Meta:
        model = Inverter
        fields = ['serial_no']


class EngineOilCreateForm(forms.ModelForm):

    product = forms.ModelChoiceField(queryset=Product.objects.filter(category__name='Engine Oil'), 
                required=True, empty_label="Select Product", 
                widget=forms.Select(attrs={'class': 'form-control'}))

    quantity = forms.IntegerField(required=True,widget=forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder':'Quantity'}))

    class Meta:
        model = EngineOil
        fields = ['product', 'quantity']


class EngineOilUpdateForm(forms.ModelForm):

    quantity = forms.IntegerField(required=True,widget=forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder':'Quantity'}))

    class Meta:
        model = EngineOil
        fields = ['quantity']


class DistilledWaterCreateForm(forms.ModelForm):

    product = forms.ModelChoiceField(queryset=Product.objects.filter(category__name='Distilled Water'), 
                required=True, empty_label="Select Product", 
                widget=forms.Select(attrs={'class': 'form-control'}))

    quantity = forms.IntegerField(required=True,widget=forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder':'Quantity'}))

    class Meta:
        model = DistilledWater
        fields = ['product', 'quantity']


class DistilledWaterUpdateForm(forms.ModelForm):

    quantity = forms.IntegerField(required=True,widget=forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder':'Quantity'}))

    class Meta:
        model = DistilledWater
        fields = ['quantity']