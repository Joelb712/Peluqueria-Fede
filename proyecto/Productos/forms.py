from django import forms
from .models import *

class ProductoForm(forms.Form):
    nombre=forms.CharField(max_length=20, label='Nombre')
    precio=forms.DecimalField(max_digits=10, decimal_places=2, label='Precio')
    descripcion=forms.CharField(max_length=255, label='Descripcion')

    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'