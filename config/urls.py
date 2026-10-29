"""Rutas principales del proyecto."""
from django.contrib import admin  # Importa el panel administrativo integrado.
from django.urls import include, path  # Herramientas para declarar rutas e incluir otras rutas.

# Cada elemento relaciona una dirección URL con una vista o conjunto de rutas.
urlpatterns = [
    path('admin/', admin.site.urls),  # Abre el panel de administración en /admin/.
    path('', include('medicamentos.urls')),  # Envía la ruta raíz y las rutas de la app a medicamentos.urls.
]
