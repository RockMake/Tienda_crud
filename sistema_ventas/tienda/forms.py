# tienda/forms.py
from django import forms
from .models import Producto, Cliente, Venta # Venta ya debería estar importado

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'correo_electronico']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre completo del cliente'}),
            'correo_electronico': forms.EmailInput(attrs={'placeholder': 'ejemplo@correo.com'}),
        }
        labels = {
            'nombre': 'Nombre del Cliente',
            'correo_electronico': 'Correo Electrónico',
        }

# Nuevo formulario para Venta
class VentaForm(forms.ModelForm):
    # Personalizar los campos para que muestren los nombres en lugar de los IDs
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), empty_label="Seleccione un cliente")
    producto = forms.ModelChoiceField(queryset=Producto.objects.all(), empty_label="Seleccione un producto")

    class Meta:
        model = Venta
        fields = ['cliente', 'producto', 'cantidad']
        widgets = {
            'cantidad': forms.NumberInput(attrs={'min': 1, 'placeholder': 'Cantidad vendida'}),
        }
        labels = {
            'cliente': 'Cliente',
            'producto': 'Producto',
            'cantidad': 'Cantidad',
        }
    # Personalizar los campos para que muestren los nombres en lugar de los IDs
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), empty_label="Seleccione un cliente")
    producto = forms.ModelChoiceField(queryset=Producto.objects.all(), empty_label="Seleccione un producto")

    class Meta:
        model = Venta
        fields = ['cliente', 'producto', 'cantidad']
        widgets = {
            'cantidad': forms.NumberInput(attrs={'min': 1, 'placeholder': 'Cantidad vendida'}),
        }
        labels = {
            'cliente': 'Cliente',
            'producto': 'Producto',
            'cantidad': 'Cantidad',
        }
    # Personalizar los campos para que muestren los nombres en lugar de los IDs
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), empty_label="Seleccione un cliente")
    producto = forms.ModelChoiceField(queryset=Producto.objects.all(), empty_label="Seleccione un producto")

    class Meta:
        model = Venta
        fields = ['cliente', 'producto', 'cantidad']
        widgets = {
            'cantidad': forms.NumberInput(attrs={'min': 1, 'placeholder': 'Cantidad vendida'}),
        }
        labels = {
            'cliente': 'Cliente',
            'producto': 'Producto',
            'cantidad': 'Cantidad',
        }   