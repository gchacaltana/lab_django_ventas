# Aplicación de ventas con Django

Repositorio que contiene aplicación de ventas con Django.

## Repositorio y Entorno Virtual

* Clonamos repositorio

```bash
git clone git@github.com:gchacaltana/lab_django_ventas.git
```

* Ingresamos a directorio

```bash
cd lab_django_ventas
```

* Creamos entorno virtual

```bash
py -m venv venv
```

* Activamos nuestro entorno virtual

```bash
source venv/Scripts/Activate
```

## Instalación Django

* Instalamos django 4.1.1 (Last Version)

```bash
pip install Django==4.1.1
```

* Verificamos los paquetes instalados en nuestro entorno virtual

```bash
pip freeze
```

* Creamos nuestro archivo de dependencias.

```bash
pip freeze > requirements.txt
```

## Proyecto Django

* Comandos django

```bash
django-admin help
```

* Creamos el proyecto django llamado "sales_admin"

```bash
django-admin startproject sales_admin
```

* Levantamos el servidor de desarrollo. Puerto por default 8000

```bash
python manage.py runserver 0.0.0.0:8080
```

## Aplicaciones

* Creamos el directorio donde crearemos las aplicaciones que conformaran el proyecto.

```bash
# cd sales_admin
mkdir applications
```

* Ingresemos al directorio "applications"

* Creamos la aplicación warehouse (Almacenes)

```bash
django-admin startapp warehouse
```

* Actualizamos atributo "name" de archivo apps.py de la aplicación warehouse.

```python
class WarehouseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # Agregamos el nombre del directorio "applications"
    name = 'applications.warehouse'
```

* Creamos la aplicación CRM (Customer Relationship Management)

```bash
django-admin startapp crm
```

* Actualizamos atributo "name" de archivo apps.py de la aplicación crm.

```python
class CrmConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # Agregamos el nombre del directorio "applications"
    name = 'applications.crm'
```

* Creamos la aplicación Sales (Ventas)

```bash
django-admin startapp sales
```

* Actualizamos atributo "name" de archivo apps.py de la aplicación sales.

```python
class SalesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # Agregamos el nombre del directorio "applications"
    name = 'applications.sales'
```

## Configuración Setting.py

* Agregamos las aplicaciones instaladas en el archivo settings.py del proyecto.

```python
INSTALLED_APPS = [
    'applications.warehouse.apps.WarehouseConfig',
    'applications.sales.apps.SalesConfig',
    'applications.crm.apps.CrmConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles'
]
```

* Configuración: language, timezone

```python
LANGUAGE_CODE = 'es-pe'

# TIME_ZONE = 'UTC'
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
TIME_ZONE = 'America/Lima'
```

* Configuración del motor de base de datos MySQL en Django.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': 'my.cnf',
            'init_command': 'SET default_storage_engine=INNODB; SET sql_mode="STRICT_TRANS_TABLES"'
        },
    }
}
```

## Instalación MySQL

* URL MySQL Community Server: https://dev.mysql.com/downloads/windows/installer/8.0.html

* Instalar MySQL. Asignar password Root. Crear cuenta de usuario admin.

* Ingresar a MySQL con usuario admin.

```bash
# mysql -V
mysql -u root -p
```

* Crear base de datos "dbstore"

```mysql
create database dbstore;
```

* Creamos archivo my.cnf para la conexión a la base de datos en la ruta raíz del proyecto.

```bash
# my.cnf
[client]
database = dbstore
user = user_admin
password = Django@456
default-character-set = utf8
```

* Asegurar que se tenga configurado la base de datos en settings.py

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': 'my.cnf',
            'init_command': 'SET default_storage_engine=INNODB; SET sql_mode="STRICT_TRANS_TABLES"'
        },
    }
}
```

* Instalamos paquete mysql en nuestro entorno virtual.

```bash
pip install mysqlclient
```

## Migrate

* Creamos archivos de migración.

```bash
py manage.py makemigrations
```

* Ejecutamos los cambios detectado en los modelos.

```bash
py manage.py migrate
```

## Aplicación Warehouse

* Agregamos los modelos de la aplicación en el archivo models.py

## Django Admin

* Creamos una cuenta super usuario para acceder al Django Admin.

```bash
py manage.py createsuperuser
```

* Podemos validar consultando la tabla auth_user de la base de datos

```mysql
select * from auth_user;
```