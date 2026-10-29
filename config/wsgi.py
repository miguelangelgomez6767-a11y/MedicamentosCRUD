"""Punto de entrada WSGI del proyecto."""
import os  # Permite configurar variables de entorno.
from django.core.wsgi import get_wsgi_application  # Crea la aplicación WSGI de Django.

# Indica el módulo de configuración que Django debe cargar.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Objeto que un servidor WSGI usa para ejecutar la aplicación.
application = get_wsgi_application()
