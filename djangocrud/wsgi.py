"""
En el archivo wsgi.py de un proyecto Django, el código que proporcionaste se encarga
de configurar y devolver la aplicación WSGI (Web Server Gateway Interface) para el proyecto
"""
import os
# Importa el módulo os, que proporciona funciones para interactuar con el sistema operativo.

from django.core.wsgi import get_wsgi_application
# Importa la función get_wsgi_application del módulo wsgi en el paquete django.core, que se utiliza para obtener la aplicación WSGI configurada para este proyecto Django.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangocrud.settings')
# Establece la variable de entorno DJANGO_SETTINGS_MODULE en 'djangocrud.settings', lo que le dice a Django qué archivo de configuración de settings debe usar.

application = get_wsgi_application()
# Obtén la aplicación WSGI para este proyecto Django, que está configurada según el archivo settings especificado.
