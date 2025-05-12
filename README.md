# Sistema de Ventas para Tienda (Django)

## Descripción

Este proyecto es una aplicación web desarrollada con el framework Django de Python para gestionar las operaciones básicas de una tienda. Permite administrar productos, clientes y registrar las ventas realizadas. La interfaz de usuario está estilizada utilizando Bootstrap 5 y los formularios se renderizan de forma optimizada con `django-crispy-forms`.

Este proyecto fue desarrollado como parte del Parcial II de Desarrollo de Aplicaciones con Acceso a Datos.

## Funcionalidades Principales

* **Gestión de Productos:**
    * Listar productos existentes.
    * Agregar nuevos productos (nombre y precio).
    * Editar información de productos existentes.
    * Eliminar productos.
* **Gestión de Clientes:**
    * Listar clientes registrados.
    * Agregar nuevos clientes (nombre y correo electrónico).
    * Editar información de clientes existentes.
    * Eliminar clientes (¡con advertencia sobre eliminación de ventas asociadas!).
* **Gestión de Ventas:**
    * Registrar nuevas ventas seleccionando un cliente y un producto existente, e indicando la cantidad.
    * Listar todas las ventas realizadas, mostrando cliente, producto, cantidad, precio unitario, total y fecha.

## Tecnologías Utilizadas

* **Backend:** Python 3.x, Django 5.x
* **Frontend:** HTML5, CSS3, Bootstrap 5.3
* **Base de Datos:** SQLite (por defecto en Django)
* **Formularios:** `django-crispy-forms` con el paquete `crispy-bootstrap5`
* **Entorno:** Python Virtual Environment (`venv`)

## Prerrequisitos

* Python 3.8 o superior (Puedes verificar con `python --version`)
* `pip` (Gestor de paquetes de Python, usualmente viene con Python)

## Instalación y Configuración

Sigue estos pasos para poner en marcha el proyecto en tu máquina local:

1.  **Clonar el Repositorio (si está en Git):**
    ```bash
    # git clone <URL_DEL_REPOSITORIO>
    # cd <NOMBRE_CARPETA_PROYECTO>
    # Si no usas Git, simplemente navega a la carpeta raíz del proyecto donde está este README.md
    cd /ruta/a/tu/proyecto/sistema_ventas
    ```

2.  **Crear y Activar un Entorno Virtual:**
    ```bash
    # Crear el entorno (puedes llamarlo 'venv' o como prefieras)
    python -m venv venv
    # Activar el entorno
    # En Windows:
    venv\Scripts\activate
    # En macOS/Linux:
    source venv/bin/activate
    ```

3.  **Instalar Dependencias:**
    Primero, asegúrate de tener el archivo `requirements.txt`. Si no lo tienes, puedes generarlo **mientras tu entorno virtual está activado** con el comando:
    ```bash
    pip freeze > requirements.txt
    ```
    Luego, instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
    *(Este archivo contendrá Django, django-crispy-forms, crispy-bootstrap5 y cualquier otra dependencia que se haya usado).*

4.  **Aplicar Migraciones de la Base de Datos:**
    Esto crea las tablas en tu base de datos SQLite basadas en los modelos definidos.
    ```bash
    python manage.py migrate
    ```

5.  **Crear un Superusuario (Administrador):**
    Este usuario te permitirá acceder al panel de administración de Django (`/admin/`).
    ```bash
    python manage.py createsuperuser
    ```
    Sigue las instrucciones para ingresar nombre de usuario, correo (opcional) y contraseña.

6.  **Ejecutar el Servidor de Desarrollo:**
    ```bash
    python manage.py runserver
    ```
    Por defecto, la aplicación estará disponible en `http://127.0.0.1:8000/`.

## Uso

Una vez que el servidor esté corriendo:

* **Panel de Administración:** Accede a `http://127.0.0.1:8000/admin/` e inicia sesión con las credenciales del superusuario. Aquí puedes gestionar directamente los datos.
* **Interfaz Principal:**
    * **Productos:** `http://127.0.0.1:8000/tienda/productos/` (Listar, Agregar, Editar, Eliminar)
    * **Clientes:** `http://127.0.0.1:8000/tienda/clientes/` (Listar, Agregar, Editar, Eliminar)
    * **Ventas:** `http://127.0.0.1:8000/tienda/ventas/` (Listar, Registrar)

Puedes usar la barra de navegación superior para moverte entre las secciones principales.

## Estructura del Proyecto (Simplificada)

sistema_ventas/       <-- Carpeta raíz del proyecto (contiene manage.py)
├── manage.py         <-- Utilidad de línea de comandos de Django
├── sistema_ventas/   <-- Carpeta de configuración del proyecto Django
│   ├── settings.py   <-- Configuración del proyecto
│   ├── urls.py       <-- URLs principales del proyecto
│   └── ...
├── tienda/           <-- Aplicación Django para la lógica de la tienda
│   ├── models.py     <-- Definición de modelos (Producto, Cliente, Venta)
│   ├── views.py      <-- Lógica de las vistas (funciones que manejan requests)
│   ├── forms.py      <-- Definición de formularios Django
│   ├── urls.py       <-- URLs específicas de la aplicación 'tienda'
│   ├── admin.py      <-- Configuración del panel de admin para los modelos
│   ├── migrations/   <-- Archivos de migración de la base de datos
│   ├── templates/    <-- Plantillas HTML
│   │   └── tienda/
│   │       ├── base.html
│   │       ├── listar_productos.html
│   │       ├── agregar_producto.html
│   │       ├── producto_confirm_delete.html
│   │       ├── ... (otras plantillas)
│   └── ...
├── venv/             <-- Carpeta del entorno virtual (si la creaste aquí)
├── db.sqlite3        <-- Archivo de la base de datos SQLite
├── requirements.txt  <-- Lista de dependencias de Python
└── README.md         <-- Este archivo

## Autor

* **Duvan leonardo ramirez vasquez**

---



