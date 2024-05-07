"""El archivo asgi.py en un proyecto Django sirve como punto de entrada para las aplicaciones ASGI 
(Asynchronous Server Gateway Interface). ASGI es una especificación para servidores web y aplicaciones
web en Python que necesitan soportar operaciones asíncronas, como WebSockets."""

#Importa el módulo os que proporciona funciones para interactuar con el sistema operativo.
import os
# Importa la función get_asgi_application del módulo asgi en el paquete django.core que se
# utiliza para obtener la aplicación ASGI configurada para este proyecto Django.
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangocrud.settings')
# Configuración del módulo de configuración de Django para este proyecto

application = get_asgi_application()
# Obtener la aplicación ASGI para este proyecto Django
