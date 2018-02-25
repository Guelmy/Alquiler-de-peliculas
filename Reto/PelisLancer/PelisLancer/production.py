from PelisLancer.settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'PelisLancerBBDD',
        'USER': 'postgres',
        'PASSWORD': 'TheMaster0124' ,
        'HOST': 'localhost',
        'PORT': 1997 ,

    }
}