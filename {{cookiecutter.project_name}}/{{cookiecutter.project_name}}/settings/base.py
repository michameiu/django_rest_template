"""
Django settings for template project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys
reload(sys)
sys.setdefaultencoding("ISO-8859-1")

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9ecu401swjo744nu^0ai*c-za$8$o1$)9gt8f)ip^$tsdkscjm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


ALLOWED_HOSTS = ['*',]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'corsheaders',
    'rest_framework',
    'social_django',
    'oauth2_provider',
    'rest_framework_social_oauth2',
    'storages',
    'client'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = '{{cookiecutter.project_name}}.urls'

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': {{cookiecutter.page_size}}

}

AUTH_USER_MODEL = 'client.MyUser'

WSGI_APPLICATION = '{{cookiecutter.project_name}}.wsgi.application'



AUTHENTICATION_BACKENDS = (

    # Others auth providers (e.g. Google, OpenId, etc)
    # Facebook OAuth2
    'social_core.backends.facebook.FacebookAppOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',

    #Google
    'social_core.backends.google.GooglePlusAuth',
    # 'social.backends.google.GoogleOAuth2'
    # django-rest-framework-social-oauth2
    'rest_framework_social_oauth2.backends.DjangoOAuth2',
    # Django
    'django.contrib.auth.backends.ModelBackend',
)
SOCIAL_AUTH_GOOGLE_PLUS_KEY = '{{cookiecutter.social_auth_google_plus_key}}'
SOCIAL_AUTH_GOOGLE_PLUS_SECRET = '{{cookiecutter.social_auth_google_plus_secret}}'
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '{{cookiecutter.social_auth_google_aouth2_key}}'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '{{cookiecutter.social_auth_google_aouth2_secret}}'


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


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = '{{cookiecutter.timezone}}'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'


MEDIA_ROOT=os.path.join(BASE_DIR,'uploads')
MEDIA_URL="/media/"

DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'
# DROPBOX_OAUTH2_TOKEN="3VjBm6r5ZtAAAAAAAAACuAqEYkiqxz6pjhVyWyvgqRR7mq8zj4JAXjSbloQrl08U"
# DROPBOX_ROOT_PATH="rayah/"
AZURE_ACCOUNT_NAME="{{cookiecutter.azure_account_name}}"
AZURE_ACCOUNT_KEY="{{cookiecutter.azure_accout_key}}"
AZURE_CONTAINER="{{cookiecutter.azure_container}}"
