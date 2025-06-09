import os
from pathlib import Path
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'default-secret-key-for-dev')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DJANGO_DEBUG', 'False').lower() == 'true'

ALLOWED_HOSTS = ['gabithex.fly.dev', 'localhost', '127.0.0.1']

# CSRF Settings
CSRF_TRUSTED_ORIGINS = ['https://gabithex.fly.dev']
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# HTTPS Settings
SECURE_SSL_REDIRECT = False  # Déjà géré par Fly.io
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

if os.getenv('DATABASE_URL'):
    import dj_database_url
    DATABASES = {
        'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Configuration pour les fichiers statiques
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Configuration pour les fichiers média
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Application definition
INSTALLED_APPS = [
    "admin_interface",
    "colorfield",

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'nene',
    'ckeditor',
    'ckeditor_uploader',
]

# Configuration de Admin Interface
X_FRAME_OPTIONS = 'SAMEORIGIN'
SILENCED_SYSTEM_CHECKS = ['security.W019']

# Thème par défaut pour admin-interface
ADMIN_INTERFACE_THEME = {
    'name': 'Gabithex Admin',
    'active': True,
    'title': 'Administration Gabithex',
    'title_color': '#F8F9FA',
    'title_visible': True,
    'logo': '',
    'logo_color': '#FFFFFF',
    'logo_visible': True,
    'css_header_background_color': '#0C4B33',
    'css_header_text_color': '#FFFFFF',
    'css_header_link_color': '#FFFFFF',
    'css_header_link_hover_color': '#C9F0DD',
    'css_module_background_color': '#44B78B',
    'css_module_text_color': '#FFFFFF',
    'css_module_link_color': '#FFFFFF',
    'css_module_link_hover_color': '#C9F0DD',
    'css_module_rounded_corners': True,
    'css_generic_link_color': '#0C3C26',
    'css_generic_link_hover_color': '#156641',
    'css_save_button_background_color': '#0C4B33',
    'css_save_button_background_hover_color': '#0C3C26',
    'css_save_button_text_color': '#FFFFFF',
    'css_delete_button_background_color': '#BA2121',
    'css_delete_button_background_hover_color': '#A41515',
    'css_delete_button_text_color': '#FFFFFF',
    'list_filter_dropdown': True,
    'related_modal_active': True,
    'related_modal_background_color': '#000000',
    'related_modal_background_opacity': '0.8',
    'related_modal_rounded_corners': True,
    'language_chooser_active': True,
}

# Middleware configuration
MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'KOTO.urls'

import os

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Assurez-vous que Django cherche ici
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


WSGI_APPLICATION = 'KOTO.wsgi.application'


LOGIN_URL = "/admin"


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static/"),
]

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]


#=======================================================
#            ENVOI DE MAIL
#============================================
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER



# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'








#==============================================

# Configuration CKEditor
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'height': 400,
        'width': '100%',
        'toolbar_Custom': [
            ['Styles', 'Format', 'Bold', 'Italic', 'Underline', 'Strike', 'SpellChecker'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Table', 'HorizontalRule'],
            ['TextColor', 'BGColor'],
            ['Smiley', 'SpecialChar'],
            ['Source'],
            ['CodeSnippet'],
        ],
        'extraPlugins': 'codesnippet',
        'codeSnippet_theme': 'monokai_sublime',
    }
}
