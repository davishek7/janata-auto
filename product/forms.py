from django import forms
from .models import Product, ProductCategory, ProductSize
from vendor.models import Vendor


class ProductForm(forms.ModelForm):

    category = forms.ModelChoiceField(queryset=ProductCategory.objects.filter(status=True), 
                required=True, empty_label="Select Category", 
                widget=forms.Select(attrs={'class': 'form-control'}))

    vendor = forms.ModelChoiceField(queryset=Vendor.objects.filter(status=True), 
                required=True, empty_label="Select Vendor", 
                widget=forms.Select(attrs={'class': 'form-control'}))

    name = forms.CharField(required=True, widget=forms.TextInput(
                    attrs={'class': 'form-control', 'placeholder':'Name'}))

    model_no = forms.CharField(required=False, widget=forms.TextInput(
                    attrs={'class': 'form-control', 'placeholder':'Model No'}))

    mrp = forms.FloatField(required=True, widget=forms.NumberInput(
                    attrs={'class': 'form-control', 'placeholder':'M.R.P.'}))

    selling_price = forms.FloatField(required=True, widget=forms.NumberInput(
                    attrs={'class': 'form-control', 'placeholder':'Selling Price'}))

    image = forms.ImageField(required=True, widget=forms.FileInput(
                    attrs={'class': 'form-control', 'placeholder':'Image'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['size'].widget.attrs.update({
            'class':'form-control'
        })

    class Meta:
        model = Product
        fields = ['category', 'vendor', 'name', 'model_no', 'size', 'mrp', 'selling_price', 'image']


class ProductCategoryForm(forms.ModelForm):

    name = forms.CharField(required=True, widget=forms.TextInput(
                    attrs={'class': 'form-control', 'placeholder':'Name'}))

    class Meta:
        model = ProductCategory
        fields = ['name']


class ProductSizeForm(forms.ModelForm):

    size = forms.IntegerField(required=True, widget=forms.Select(choices=ProductSize.PRODUCT_SIZE_CHOICES,
                    attrs={'class': 'form-control', 'placeholder':'Size'}))

    category = forms.ModelChoiceField(queryset=ProductCategory.objects.all(), 
                required=True, empty_label="Select Category", 
                widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = ProductSize
        fields = ['size', 'category']