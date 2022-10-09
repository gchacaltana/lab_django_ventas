from django import forms
from .models import ProductCategory

class ProductCategoryForm(forms.ModelForm):
    """
    Formulario para el Modelo ProductCategory.

    Creamos formulario con tres inputs.
    """

    code = forms.CharField(
        #label = "Código Cat",
        label=ProductCategory._meta.get_field('code').verbose_name,
        max_length= ProductCategory._meta.get_field('code').max_length,
        help_text=('Escriba el código de categoría'),
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'code', 'placeholder': 'Código'}))

    name = forms.CharField(
        label=ProductCategory._meta.get_field('name').verbose_name,
        max_length=ProductCategory._meta.get_field('name').max_length,
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}))

    percent_discount = forms.CharField(
        required=True,
        label=ProductCategory._meta.get_field('percent_discount').verbose_name,
        max_length=ProductCategory._meta.get_field('percent_discount').max_length,
        widget=forms.NumberInput(attrs={'min':0, 'max':10, 'class': 'form-control', 'id': 'percent_discount'}))

    class Meta:
        model = ProductCategory
        fields = "__all__"