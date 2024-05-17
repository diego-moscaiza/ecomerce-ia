# Backend para tienda online con Django

## Configuración inicial

### 1.- Crear entorno virtual aislado (venv) con Python para este proyecto

Colocamos este script para crear la carpeta llamada "venv" con todas las configuraciones de python.
`py -m venv venv`

### 2.- Activar venv

En el CMD (windows) debe dirigirse a la siguiente ruta del proyecto

`.\venv\Scripts\activate`

O usando Visual Studio Code, puede presione `Ctrl + Shift + P` y escribir:

`Python: Seleccionar intérprete`

Y seleccionar la opción que diga `Python "tu-version" ('venv':venv)`

Y en tu consola te debe aparecer de la siguiente forma:

`(venv) C:\User\...\...`

- Para **desactivarlo** puedes usar: `.\venv\Scripts\deactivate`

### 3.- Instalar Django

Instalamos Django con la siguiente línea:
`pip install django`

Comprobamos si ya está instalado:
`django-admin --version`

Y te aparecerá la versión de Django que tienes instaladas.

### 4.- Crear proyecto base de Django

Para configurar todos nuestro proyecto es necesario crear un proyecto base

El comando para crearlo empieza así:
`django-admin startproject`

Luego se coloca el nombre del proyecto base y un punto para crearlo fuera de la carpeta "venv"

Y quedaría de esta forma: `django-admin startproject admin .`


### 5.- Ejecutar el servidor del proyecto

Ingresamos este comando:
`python manage.py runserver`

### 6.- Creamos una aplicacion

Ingresamos este comando y la ultima palabra es el nombre de la aplicación.
En este caso se llama "tasks" o tareas.
`python manage.py startapp tasks`

### 7.- Instalamos Django REST Framework

Ingresamos este comando:
`pip install djangorestframework`

### 8.- Integramos el módulo para conexión de servidores

Ingresamos este comando:
`pip install django-cors-headers`

Se debe de conectar los servidores de frontend y backend de manera manual ya que luego puede haber problemas de CORS.

### 9.- Migrar integraciones

Esto es para migrar todas las integraciones:
`python manage.py makemigrations`

Para migrar solo las integraciones de un lugar especifico se declara el nombre:
`python manage.py makemigrations tasks`

### 10.- Ejecutar integraciones migradas

Esto es para ejecutar todas las migraciones:
`python manage.py migrate`

Para ejecutar solo las migraciones de un lugar especifico se declara el nombre:
`python manage.py migrate tasks`


## Panel de Administrador de Django

### 1.- Creación de SuperUsuario

Ingresamos este comando:
`python manage.py createsuperuser`

- En nuestro caso será: admin-"tu-nombre"
- Luego debe ingresar su correo electronico
- Y la contraseña debe ser de 8 caracteres minimo, por ejemplo: admin-"tu-nombre"
- Se tiene que ingresar la contrase 2 veces.
- Puedes colocar una contraseña corta de todas formas ya que sale un mensaje para pasarlo de todas formas.


## Documentacion automatica de un proyecto

Ingresamos este comando:
`pip install coreapi`

