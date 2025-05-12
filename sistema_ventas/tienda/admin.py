from django.contrib import admin
from .models import Cliente, Producto, Venta

class VentaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'producto', 'cantidad', 'fecha_venta', 'total_venta')
    list_filter = ('fecha_venta', 'cliente', 'producto')
    search_fields = ('cliente__nombre', 'producto__nombre')

admin.site.register(Cliente)
admin.site.register(Producto)       
admin.site.register(Venta, VentaAdmin)