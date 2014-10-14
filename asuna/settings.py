"""
Django settings for asuna project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wi077bxa2#42&q3d4(4$gu4^17$(vg$g#_nz!4u^uzip5hvz2j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'asuna.urls'

WSGI_APPLICATION = 'asuna.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'


# Added by rog
#STATICFILES_FINDERS = (
#    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.FileSystemFinder',
#)


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth'
)


# Grappelli specific
GRAPPELLI_ADMIN_TITLE = 'Broknet'
# GRAPPELLI_AUTOCOMPLETE_LIMIT # Number of items to show with autocomplete drop–downs.
# GRAPPELLI_AUTOCOMPLETE_SEARCH_FIELDS # A dictionary containing search patterns for models you cannot (or should not) alter.
# Set to True if you want to activate the switch user functionality.
# GRAPPELLI_SWITCH_USER = True
# A function which defines if a User is able to switch to another User (returns either True or False). Defaults to all superusers.
# GRAPPELLI_SWITCH_USER_ORIGINAL = True
# A function which defines if a User is a valid switch target (returns either True or False). Defaults to all staff users, excluding superusers.
# GRAPPELLI_SWITCH_USER_TARGET = True
# Replaces HTML5 input types (search, email, url, tel, number, range, date, month, week, time, datetime, datetime-local, color)
# due to browser inconsistencies. Set to False in order to not replace the mentioned input types.
# GRAPPELLI_CLEAN_INPUT_TYPES



