from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields ='__all__'
        widgets={
            'nombre_cliente':forms.TextInput(attrs={'placeholder':'Ingrese su Nombre'}) ,
            'apellido_cliente':forms.TextInput(attrs={'placeholder':'Ingrese su Apellido'}) ,
            'fecha_nacimiento_cliente': forms.DateInput(attrs={'type': 'date'}),
            'telefono_cliente': forms.TextInput(attrs={'placeholder':'+54 387-123-1234','required':True}),
            'correo_cliente':forms.EmailInput(attrs={'required':True , 'placeholder':'Correo Electronico'})
                }
        help_texts = {}