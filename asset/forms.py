from django import forms
from product.models import Product
from .models import Battery, EngineOil, DistilledWater


class BatteryCreateForm(forms.ModelForm):

    product = forms.ModelChoiceField(queryset=Product.objects.filter(category__name='Battery'), 
                required=True, empty_label="Select Product", 
                widget=forms.Select(attrs={'class': 'form-control'}))

    serial_no = forms.CharField(required=True, widget=forms.TextInput(
                attrs={'class': 'form-control', 'placeholder':'Serial No'}))

    model_no = forms.CharField(required=True, widget=forms.TextInput(
                    attrs={'class': 'form-control', 'placeholder':'Model No'}))

    image = forms.ImageField(required=True, widget=forms.FileInput(
                attrs={'class': 'form-control', 'placeholder':'Image'}))

    def clean_serial_no(self):
        serial_no = self.cleaned_data.get('serial_no')
        if '/' not in serial_no:
            raise ValidationError("'/' must be in serial no")
        return serial_no

    class Meta:
        model = Battery
        fields = ['product', 'serial_no', 'model_no', 'image']


class EngineOilCreateForm(forms.ModelForm):

    product = forms.ModelChoiceField(queryset=Product.objects.filter(category__name='Engine Oil'), 
                required=True, empty_label="Select Product", 
                widget=forms.Select(attrs={'class': 'form-control'}))


    quantity = forms.IntegerField(required=True,widget=forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder':'Quantity'}))

    class Meta:
        model = EngineOil
        fields = ['product', 'quantity']


class DistilledWaterCreateForm(forms.ModelForm):

    product = forms.ModelChoiceField(queryset=Product.objects.all(), 
                required=True, empty_label="Select Product", 
                widget=forms.Select(attrs={'class': 'form-control'}))

    quantity = forms.IntegerField(required=True,widget=forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder':'Quantity'}))

    class Meta:
        model = DistilledWater
        fields = ['product', 'quantity']