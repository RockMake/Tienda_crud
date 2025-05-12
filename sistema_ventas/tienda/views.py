# tienda/views.py
from django.shortcuts import render, redirect, get_object_or_404
# Asegúrate de tener todos los modelos y formularios importados 
from .models import Producto, Cliente, Venta
from .forms import ProductoForm, ClienteForm, VentaForm # Importamos VentaForm

# ... (vistas de producto y cliente existentes) ...
def listar_productos(request):
    productos = Producto.objects.all()
    contexto = {'productos': productos}
    return render(request, 'tienda/listar_productos.html', contexto)

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()
    contexto = {'form': form}
    return render(request, 'tienda/agregar_producto.html', contexto)

def listar_clientes(request):
    clientes = Cliente.objects.all()
    contexto = {'clientes': clientes}
    return render(request, 'tienda/listar_clientes.html', contexto)

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    contexto = {'form': form}
    return render(request, 'tienda/agregar_cliente.html', contexto)

def registrar_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save() # Guarda la nueva venta
            return redirect('listar_ventas') # Redirige a la lista de ventas
    else:
        form = VentaForm() # Crea un formulario vacío

    contexto = {'form': form}
    return render(request, 'tienda/registrar_venta.html', contexto)

def listar_ventas(request):
    # Usamos select_related para optimizar la consulta y traer los datos
    # de Cliente y Producto en la misma consulta a la base de datos.
    ventas = Venta.objects.select_related('cliente', 'producto').all().order_by('-fecha_venta')
    contexto = {'ventas': ventas}
    return render(request, 'tienda/listar_ventas.html', contexto)

def editar_producto(request, pk):
    # Obtenemos el producto por su ID (pk) o mostramos un error 404 si no existe
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        # Pasamos la instancia del producto al formulario para que se actualice
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        # Si es GET, creamos el formulario con los datos de la instancia del producto
        form = ProductoForm(instance=producto)

    contexto = {
        'form': form,
        'producto': producto # Opcional: pasar el objeto por si quieres mostrar info extra
    }
    # Reutilizamos la plantilla de agregar, pero podríamos crear una específica si quisiéramos
    return render(request, 'tienda/agregar_producto.html', contexto)

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')

    # Si es GET, mostramos la confirmación
    contexto = {'producto': producto}
    return render(request, 'tienda/producto_confirm_delete.html', contexto)

def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm(instance=cliente)
    contexto = {'form': form, 'cliente': cliente}
    # Reutilizamos la plantilla agregar_cliente
    return render(request, 'tienda/agregar_cliente.html', contexto)

def eliminar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        # Considerar qué pasa con las ventas de este cliente si se elimina
        # Por defecto (on_delete=models.CASCADE), las ventas asociadas se eliminarán.
        # Si quieres otro comportamiento, deberías cambiar el modelo.
        cliente.delete()
        return redirect('listar_clientes')
    contexto = {'cliente': cliente}
    return render(request, 'tienda/cliente_confirm_delete.html', contexto)