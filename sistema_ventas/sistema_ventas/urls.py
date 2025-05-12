# sistema_ventas/urls.py
from django.contrib import admin
from django.urls import path, include # Asegúrate de que 'include' esté importado

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tienda/', include('tienda.urls')), # Incluye las URLs de tu app tienda
    # Puedes agregar una ruta para la página de inicio del sitio si quieres
    # path('', alguna_vista_de_inicio, name='inicio_sitio'),
]