"""
Django settings for CHF project.

Generated by 'django-admin startproject' using Django 1.9.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hrg#-fktrmp63su2lqeur99()7@anz%@e777-2ap89%75fz9kz'

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'polymorphic',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_mako_plus',
    'account',
    'catalog',
    'event',
    'homepage',
    'manager',
    'api',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'CHF.shopping_cart.ShoppingCartMiddleware', #need to write the function into the shopping_cart.py file before allowing this middleware
    'django_mako_plus.RequestInitMiddleware',

]

DEBUG_PROPAGATE_EXCEPTIONS = DEBUG  # never set this True on a live site
LOGGING = {
   'version': 1,
   'disable_existing_loggers': True,
   'formatters': {
       'simple': {
           'format': '%(levelname)s %(message)s'
       },
   },
   'handlers': {
       'console':{
           'level':'DEBUG',
           'class':'logging.StreamHandler',
           'formatter': 'simple'
       },
   },
   'loggers': {
       'django_mako_plus': {
           'handlers': ['console'],
           'level': 'DEBUG',
           'propagate': False,
   },
       # 'django.db.backends': {
       #             'level': 'DEBUG',
       #             'handlers': ['console'],
       #         },
   },
}


ROOT_URLCONF = 'CHF.urls'

TEMPLATES = [
  {
    'BACKEND': 'django_mako_plus.MakoTemplates',
    'OPTIONS': {
      # functions to automatically add variables to the params/context before templates are rendered
      'CONTEXT_PROESSORS': [
        'django.template.context_processors.static',            # adds "STATIC_URL" from settings.py
        'django.template.context_processors.request',           # adds "request" object
        'django.contrib.auth.context_processors.auth',          # adds "user" and "perms" objects
        'django_mako_plus.context_processors.settings',         # adds "settings" dictionary
      ],

      # identifies where the Mako template cache will be stored, relative to each app
      'TEMPLATES_CACHE_DIR': '.cached_templates',

      # the default app and page to render in Mako when the url is too short
      'DEFAULT_PAGE': 'index',
      'DEFAULT_APP': 'homepage',

      # the default encoding of template files
      'DEFAULT_TEMPLATE_ENCODING': 'utf-8',

      # these are included in every template by default - if you put your most-used libraries here, you won't have to import them exlicitly in templates
      'DEFAULT_TEMPLATE_IMPORTS': [
        'import os, os.path, re, json',
      ],

      # see the DMP online tutorial for information about this setting
      'URL_START_INDEX': 0,

      # whether to send the custom DMP signals -- set to False for a slight speed-up in router processing
      # determines whether DMP will send its custom signals during the process
      'SIGNALS': True,

      # whether to minify using rjsmin, rcssmin during 1) collection of static files, and 2) on the fly as .jsm and .cssm files are rendered
      # rjsmin and rcssmin are fast enough that doing it on the fly can be done without slowing requests down
      'MINIFY_JS_CSS': True,

      # the name of the SASS binary to run if a .scss file is newer than the resulting .css file
      # happens when the corresponding template.html is accessed the first time after server startup
      # if DEBUG=False, this only happens once per file after server startup, not for every request
      # specify the binary in a list below -- even if just one item (see subprocess.Popen)
      'SCSS_BINARY': [ '/usr/bin/env', 'scss', '--unix-newlines' ],

      # see the DMP online tutorial for information about this setting
      # it can normally be empty
      'TEMPLATES_DIRS': [
        # '/var/somewhere/templates/',
      ],
    },
  },

  # you'll likely already have the DjangoTemplates settings here
]

WSGI_APPLICATION = 'CHF.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

AUTH_USER_MODEL = 'account.User'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'CHF',
        'USER': 'postgres',
        'PASSWORD': 'Password1',
        'HOST': 'localhost',
    },
  # 'default': {
  #   'ENGINE': 'django.db.backends.sqlite3',
  #   'NAME': 'sqlite.db',
  # },
}
# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
   # SECURITY WARNING: this next line must be commented out at deployment
   BASE_DIR,  
)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')  


