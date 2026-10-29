"""Configuración general del proyecto Django."""
from pathlib import Path  # Herramienta para construir rutas de archivos de forma portable.

# Calcula la carpeta raíz del proyecto a partir de la ubicación de este archivo.
BASE_DIR = Path(__file__).resolve().parent.parent

# Clave secreta usada por Django para funciones de seguridad; no publicar en producción.
SECRET_KEY = 'django-insecure-#k=8^(&3g3t5s3_7=^t0np28(3aoe$((0#0b@xiy9jfr%*lq4u'

# Activa los mensajes detallados de error durante el desarrollo; en producción debe ser False.
DEBUG = True

# Lista de dominios permitidos; debe configurarse al desplegar con DEBUG=False.
ALLOWED_HOSTS = []

# Aplicaciones integradas de Django y aplicación propia del inventario.
INSTALLED_APPS = [
    'django.contrib.admin',  # Panel administrativo.
    'django.contrib.auth',  # Usuarios, grupos y permisos.
    'django.contrib.contenttypes',  # Seguimiento de tipos de modelos.
    'django.contrib.sessions',  # Manejo de sesiones de usuario.
    'django.contrib.messages',  # Mensajes temporales entre solicitudes.
    'django.contrib.staticfiles',  # Gestión de CSS, JavaScript e imágenes estáticas.
    'medicamentos',  # Aplicación que implementa el CRUD de medicamentos.
]

# Middleware: componentes que procesan solicitudes y respuestas HTTP.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Añade protecciones de seguridad.
    'django.contrib.sessions.middleware.SessionMiddleware',  # Habilita sesiones.
    'django.middleware.common.CommonMiddleware',  # Funciones comunes para solicitudes.
    'django.middleware.csrf.CsrfViewMiddleware',  # Protección CSRF en formularios.
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Identifica al usuario autenticado.
    'django.contrib.messages.middleware.MessageMiddleware',  # Habilita mensajes temporales.
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Mitiga ataques de clickjacking.
]

# Archivo que contiene las rutas principales del sitio.
ROOT_URLCONF = 'config.urls'

# Configuración del motor de plantillas HTML de Django.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Motor de plantillas Django.
        'DIRS': [],  # No define carpetas globales adicionales de plantillas.
        'APP_DIRS': True,  # Busca plantillas dentro de las aplicaciones instaladas.
        'OPTIONS': {
            'context_processors': [  # Datos globales disponibles en las plantillas.
                'django.template.context_processors.request',  # Agrega el objeto request.
                'django.contrib.auth.context_processors.auth',  # Agrega información de autenticación.
                'django.contrib.messages.context_processors.messages',  # Agrega mensajes.
            ],
        },
    },
]

# Punto de entrada WSGI para servidores web compatibles.
WSGI_APPLICATION = 'config.wsgi.application'

# Importa utilidades para leer la variable DATABASE_URL y configurar una base de datos externa.
import os
import dj_database_url

# Si existe DATABASE_URL, configura la base de datos indicada por esa variable.
if os.environ.get('DATABASE_URL'):
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ['DATABASE_URL'],  # URL de conexión de la base de datos.
            conn_max_age=600  # Mantiene conexiones persistentes hasta 600 segundos.
        )
    }
else:
    # Si no existe DATABASE_URL, usa SQLite en el archivo db.sqlite3 del proyecto.
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',  # Motor de base de datos SQLite.
            'NAME': BASE_DIR / 'db.sqlite3',  # Ruta del archivo de base de datos.
        }
    }

# Validadores de contraseñas usados por el sistema de autenticación de Django.
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},  # Evita contraseñas parecidas a datos del usuario.
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},  # Exige una longitud mínima.
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},  # Rechaza contraseñas comunes.
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},  # Rechaza contraseñas solo numéricas.
]

# Idioma y opciones de internacionalización.
LANGUAGE_CODE = 'en-us'  # Idioma global predeterminado de Django.
TIME_ZONE = 'UTC'  # Zona horaria predeterminada del proyecto.
USE_I18N = True  # Habilita internacionalización.
USE_TZ = True  # Usa fechas y horas conscientes de zona horaria.

# Prefijo URL para archivos estáticos, como CSS, JavaScript e imágenes.
STATIC_URL = 'static/'

# Configuración escrita en el proyecto para correo; MAILERS no es el ajuste estándar de Django.
# Para configurar el correo estándar de Django normalmente se usa EMAIL_BACKEND.
MAILERS = {
    'default': {
        'BACKEND': 'django.core.mail.backends.console.EmailBackend',  # Pretende mostrar correos en consola.
    },
}
