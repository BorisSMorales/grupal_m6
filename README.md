# Guía: Mostrar contenido dinámico desde una base de datos SQLite en una aplicación web con Django
## Paso 1: Creación del entorno virtual
1. Abre una terminal o línea de comandos en tu sistema.
2. Navega hasta el directorio donde deseas crear tu proyecto Django.
3. Ejecuta el siguiente comando para crear un nuevo entorno virtual:
```sh
python -m venv nombre_entorno_virtual
```
Asegúrate de reemplazar "nombre_entorno_virtual" con el nombre que deseas darle a tu entorno virtual.

4. Activa el entorno virtual ejecutando el siguiente comando:
- En Windows:
```sh
nombre_entorno_virtual\Scripts\activate
```
- En macOS/Linux:
```sh
source nombre_entorno_virtual/bin/activate
```
Verás que el prompt de la terminal cambia para indicar que el entorno virtual está activo.

## Paso 2: Instalación de Django y creación del proyecto

1. Asegúrate de que tu entorno virtual esté activo.

2. Ejecuta el siguiente comando para instalar Django:

```sh
pip install django
```
3. Crea un nuevo proyecto de Django ejecutando el siguiente comando:

```sh
django-admin startproject nombre_proyecto
```
Esto creará una carpeta con el nombre del proyecto y generará los archivos necesarios.

4. Navega al directorio del proyecto Django:
```sh
cd nombre_proyecto
```
## Paso 3: Configuración de la base de datos SQLite

1. Abre el archivo settings.py en un editor de texto.

2. En la sección [DATABASES], actualiza la configuración [default] con la ruta absoluta de tu archivo SQLite3:
```sh
python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/ruta/absoluta/hacia/nombre_base_datos.sqlite3',
    }
}
```
Asegúrate de reemplazar "/ruta/absoluta/hacia/" con la ubicación real de tu archivo SQLite3.

## Paso 4: Definición de modelos en Django

1. Crea una nueva aplicación Django dentro del proyecto ejecutando el siguiente comando:

```sh
python manage.py startapp nombre_app
```
2. Abre el archivo models.py en la carpeta de la aplicación recién creada.
3. Define los modelos que correspondan a las tablas de tu base de datos SQLite. Por ejemplo, para la tabla "Productos" que creamos anteriormente, puedes agregar el siguiente código:

```python
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    cantidad = models.IntegerField()
```

## Paso 5: Ejecución de migraciones y creación de superusuario

1. Ejecuta las migraciones para crear las tablas en la base de datos:

```sh
python manage.py makemigrations
python manage.py migrate
```
2. Crea un superusuario para acceder al panel de administración de Django:

```sh
python manage.py createsuperuser
```
Sigue las instrucciones para proporcionar un nombre de usuario, dirección de correo electrónico y contraseña.

## Paso 6: Creación de vistas y plantillas

1. Abre el archivo views.py en la carpeta de la aplicación.

2. Define las vistas necesarias para mostrar el contenido dinámico desde la base de datos. Puedes utilizar el ORM de Django para recuperar los datos de la tabla. Por ejemplo:

```sh
python
from django.shortcuts import render
from .models import Producto

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})
```
3. Crea una plantilla HTML en la carpeta templates de la aplicación. Por ejemplo, crea un archivo llamado lista_productos.html y utiliza la sintaxis de plantillas de Django para mostrar los datos:
```sh
html
{% for producto in productos %}
    <h3>{{ producto.nombre }}</h3>
    <p>Precio: ${{ producto.precio }}</p>
    <p>Cantidad: {{ producto.cantidad }}</p>
{% endfor %}
```
## Paso 7: Configuración de URLs

1. Abre el archivo urls.py en la carpeta de la aplicación.
2. Agrega una URL para acceder a la vista que creaste anteriormente. Por ejemplo:
```sh
python
from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.lista_productos, name='lista_productos'),
]
```
## Paso 8: Ejecución de la aplicación

1. Asegúrate de que tu entorno virtual esté activo y de que te encuentres en el directorio del proyecto Django.

2. Inicia el servidor de desarrollo de Django ejecutando el siguiente comando:
```sh
python manage.py runserver
```
3. Abre un navegador web y visita la URL http://localhost:8000/productos/ para ver el contenido dinámico generado desde tu base de datos SQLite.

✨Siguiendo estos pasos, se puede crear un entorno virtual, instalar Django, configurar la base de datos SQLite y mostrar contenido dinámico en una aplicación web utilizando Django✨

_Creado por grupo 4_


