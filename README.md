✨Siguiendo esta guía se puede levantar un formulario desde Django usando Forms y Models.✨

#Paso 1: Configuración inicial

    Asegúrate de tener Django instalado en tu entorno de desarrollo.
    Crea un nuevo proyecto Django utilizando el comando django-admin startproject nombre_proyecto.
    Accede al directorio del proyecto usando cd nombre_proyecto.

Paso 2: Creación del modelo

    Define el modelo en el archivo models.py de tu aplicación.
    Importa models de django.db y crea una clase que herede de models.Model.
    Dentro de la clase, define los campos del modelo utilizando los diferentes tipos de campos proporcionados por Django, como CharField, IntegerField, etc.

Paso 3: Migraciones

    Genera las migraciones para tu modelo ejecutando python manage.py makemigrations en la línea de comandos.
    Aplica las migraciones con el comando python manage.py migrate.

Paso 4: Creación del formulario

    Crea un archivo llamado forms.py en tu aplicación.
    Importa forms de django y define una clase para tu formulario que herede de forms.ModelForm.
    Especifica el modelo al que está asociado el formulario utilizando la variable Meta dentro de la clase del formulario.

Paso 5: Vistas

    Abre el archivo views.py de tu aplicación.
    Importa el formulario que creaste en el paso anterior.
    Define una función de vista que maneje la lógica para mostrar y procesar el formulario.
    En la función de vista, crea una instancia del formulario y pásala al contexto del template.

Paso 6: Templates

    Crea un directorio llamado templates en el directorio de tu aplicación.
    Dentro del directorio templates, crea otro directorio con el nombre de tu aplicación.
    Crea un archivo HTML dentro del directorio de tu aplicación y define el formulario utilizando las etiquetas y campos proporcionados por Django.

Paso 7: URLconf

    Abre el archivo urls.py en el directorio de tu proyecto.
    Importa la función de vista creada en el paso anterior.
    Agrega una ruta URL que corresponda a la función de vista y asóciala a una URL específica.

Paso 8: Ejecución

    Ejecuta el servidor de desarrollo de Django con el comando python manage.py runserver.
    Abre un navegador web y accede a la URL asociada a tu formulario.
    Deberías poder ver y enviar el formulario, y los datos enviados deben almacenarse en la base de datos.
    
    
_Creado por grupo 4_



