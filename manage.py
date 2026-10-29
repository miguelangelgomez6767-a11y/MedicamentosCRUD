#!/usr/bin/env python
# Indica que este archivo debe ejecutarse con Python.
"""Utilidad de línea de comandos de Django para tareas administrativas."""
import os  # Permite configurar variables de entorno del proceso.
import sys  # Permite leer los argumentos escritos en la terminal.


def main():  # Función principal que prepara y ejecuta los comandos de Django.
    """Ejecuta tareas administrativas."""
    # Le indica a Django qué archivo contiene la configuración del proyecto.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:  # Intenta importar el ejecutor de comandos de Django.
        from django.core.management import execute_from_command_line
    except ImportError as exc:  # Maneja el caso en que Django no esté instalado o disponible.
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? "
            "Did you forget to activate a virtual environment?"
        ) from exc
    # Ejecuta el comando que el usuario pasó por la terminal.
    execute_from_command_line(sys.argv)


# Solo llama a main cuando este archivo se ejecuta directamente.
if __name__ == '__main__':
    main()
