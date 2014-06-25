"""
Django settings for persdic project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import os.path
from pymongo import Connection
from pymongo.errors import ConnectionFailure
import django_mongodb_engine as dme
import json
#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()

"""try:
  client = Connection(host="localhost", port=27017)
except ConnectionFailure, e:
  sys.stderr.write("Could not connect to MongoDB: %s" % e)
  sys.exit(1)
dbh = client["mydb3"]
"""
#with open(os.path.expanduser('~/environment.json')) as f:
  #env = json.load(f)


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
#STATICFILES_DIRS = [os.path.join(BASE_DIR, "static"),'persdicapp/static/']

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY ='pe%a#xmp$k%w5(=p2m3rhugutw1*2-g1xjfidjpe1iq!n(2t$!'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    #'django_mongodb_engine'
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'persdicapp',
    'djangotoolbox',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
)

ROOT_URLCONF = 'persdic.urls'

#WSGI_APPLICATION = 'persdic.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django_mongodb_engine',
        'NAME': 'mydb3',
        #'HOST':dbh,
        'PORT':27017,
        #'USERNAME':'bluebird',
	#'PASSWORD':'mazdak'
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
SOCIAL_AUTH_MODELS = 'social_auth.db.mongoengine_models' #social_auth.db.mongoengine_models'


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
