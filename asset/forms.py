from django import forms
from product.models import Product
from .models import Battery, EngineOil, DistilledWater


class BatteryCreateForm(forms.ModelForm):

    product = forms.ModelChoiceField(queryset=Product.objects.all(), 
                required=True, empty_label="Select Product", 
                widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))

    serial_no = forms.CharField(required=True, widget=forms.TextInput(
                attrs={'class': 'form-control form-control-sm', 'placeholder':'Serial No'}))

    image = forms.ImageField(required=True, widget=forms.FileInput(
                attrs={'class': 'form-control form-control-sm', 'placeholder':'Image'}))

    def clean_serial_no(self):
        serial_no = self.cleaned_data.get('serial_no')
        if len(serial_no) == 0:
            raise ValidationError('Serial No can not be blank.')
        return serial_no

    class Meta:
        model = Battery
        fields = ['product', 'serial_no', 'image']


BatteryCreateFormSet = forms.modelformset_factory(Battery, form=BatteryCreateForm)


class EngineOilCreateForm(forms.ModelForm):

    product = forms.ModelChoiceField(queryset=Product.objects.all(), 
                required=True, empty_label="Select Product", 
                widget=forms.Select(attrs={'class': 'form-control'}))

    size = forms.CharField(required=True, widget=forms.Select(
                choices = EngineOil.ENGINE_OIL_CHOICES,
                attrs={'class': 'form-control'}))

    quantity = forms.IntegerField(required=True,widget=forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder':'Quantity'}))

    class Meta:
        model = EngineOil
        fields = ['product', 'size', 'quantity']


class DistilledWaterCreateForm(forms.ModelForm):

    product = forms.ModelChoiceField(queryset=Product.objects.all(), 
                required=True, empty_label="Select Product", 
                widget=forms.Select(attrs={'class': 'form-control'}))

    size = forms.CharField(required=True, widget=forms.Select(
                choices = DistilledWater.DISTILLED_WATER_CHOICES,
                attrs={'class': 'form-control'}))

    quantity = forms.IntegerField(required=True,widget=forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder':'Quantity'}))

    class Meta:
        model = DistilledWater
        fields = ['product', 'size', 'quantity']