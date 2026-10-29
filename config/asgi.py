"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.1/howto/deployment/asgi/
"""

"""Punto de entrada ASGI del proyecto."""
import os  # Permite configurar variables de entorno.
from django.core.asgi import get_asgi_application  # Crea la aplicación ASGI de Django.

# Indica el módulo de configuración que Django debe cargar.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Objeto que un servidor ASGI usa para ejecutar la aplicación.
application = get_asgi_application()

