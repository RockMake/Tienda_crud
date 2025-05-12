from django.db import models
from django.utils import timezone

class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    correo_electronico = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=200)       
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha_venta = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Venta de {self.cantidad} x {self.producto.nombre} a {self.cliente.nombre} el {self.fecha_venta.strftime('%Y-%m-%d %H:%M')}"

    def total_venta(self):
        return self.cantidad * self.producto.precio