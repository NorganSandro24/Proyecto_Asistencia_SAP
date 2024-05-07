from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# Define el directorio base del proyecto

SECRET_KEY = 'django-insecure-(oa(omhdw75#3qzk_p-6zfdfmvj#%tn=oci!ww+ssog(ib%-o='
# Clave secreta para seguridad, mantenla privada

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# Configuración para activar o desactivar el modo de depuración

ALLOWED_HOSTS = []
# Lista de hosts permitidos para el proyecto Django

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tasks'
]
# Aplicaciones instaladas en el proyecto Django

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# Middleware utilizado en el proyecto Django

ROOT_URLCONF = 'djangocrud.urls'
# Configuración de la URL raíz del proyecto Django

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# Configuración de las plantillas utilizadas en el proyecto Django

WSGI_APPLICATION = 'djangocrud.wsgi.application'
# Configuración de la aplicación WSGI para el proyecto Django

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# Configuración de la base de datos utilizada en el proyecto Django

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
# Configuración de validación de contraseñas en el proyecto Django

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/
LANGUAGE_CODE = 'en-us'
# Configuración del código de idioma utilizado en el proyecto Django

TIME_ZONE = 'UTC'
# Configuración de la zona horaria utilizada en el proyecto Django

USE_I18N = True
USE_TZ = True
# Configuración para habilitar el soporte de internacionalización en el proyecto Django

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_URL = 'static/'
# URL base para archivos estáticos como CSS, JavaScript e imágenes

LOGIN_URL = '/signin'
# URL de inicio de sesión para redireccionar usuarios no autenticados

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# Tipo de campo de clave primaria predeterminado utilizado en el proyecto Django
