from django.urls import path
from . import views

urlpatterns = [
    # URLs de Productos
    path('productos/', views.listar_productos, name='listar_productos'),
    path('productos/agregar/', views.agregar_producto, name='agregar_producto'),
    path('productos/editar/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),

    # URLs de Clientes
    path('clientes/', views.listar_clientes, name='listar_clientes'),
    path('clientes/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('clientes/editar/<int:pk>/', views.editar_cliente, name='editar_cliente'),
    path('clientes/eliminar/<int:pk>/', views.eliminar_cliente, name='eliminar_cliente'),

    # URLs de Ventas
    path('ventas/', views.listar_ventas, name='listar_ventas'),
    path('ventas/registrar/', views.registrar_venta, name='registrar_venta'),
]