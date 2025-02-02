"""
Django settings for djreact project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from datetime import timedelta

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'YOUR SECRET KEY HERE'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG variable is set to True at development level but set to False at production level
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
# installed application
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # LOCAL APPLICATIONS INSTALLATIONS
    'frontend',
    'lead',
    'accounts',
    
    # THIRD PARTY APPLICATION INSTALLATIONS
    'rest_framework', # since we are using the Django Rest framework
    'knox', 

]

#DJANGO REST FRAMEWORK DEFAULT AUTHENTICATION CLASS DEFINITION => USING THE "KNOX token authentication"
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ('knox.auth.TokenAuthentication',)
    
}

# Setting the REST KNOX token TTL (Time To Live)
from datetime import timedelta
from rest_framework.settings import api_settings
REST_KNOX = {
  'SECURE_HASH_ALGORITHM': 'cryptography.hazmat.primitives.hashes.SHA512',
  'AUTH_TOKEN_CHARACTER_LENGTH': 64,
  'TOKEN_TTL': timedelta(hours=10),
#   'USER_SERIALIZER': 'knox.serializers.UserSerializer',
  'TOKEN_LIMIT_PER_USER': None, # no limit , u can generate as many token as u want per user , but default is None
  'AUTO_REFRESH': False,
  'EXPIRY_DATETIME_FORMAT': api_settings.DATETIME_FORMAT
  
}





# middleware configurations
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]



#URL configuration for the entry point of the web application
ROOT_URLCONF = 'djreact.urls'



# templates configurations
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


# configuration needed for production level/delpoyment stage
WSGI_APPLICATION = 'djreact.wsgi.application'



# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
# Database configuration for the project
DATABASES = {
    'default': {
        'ENGINE': 'your-db-engine', 
        'NAME' : 'your-db-name',
        'USER' : 'your-username',
        'PASSWORD' : 'your-password'

    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'


# rest_framework.# permissions.IsAuthenticatedclass, which enforces that only users logged
# in via Django’s built-in user system
# MEANING : Your be able to use the rest_framework api if not logged in as user

# THE PERMISSION CLASS ALREADY DEFINED IN THE VIEW CLASS

