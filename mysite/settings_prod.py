from .settings import *

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'NAME': 'poznavayka',
       'USER': 'poznavaykauser',
       'PASSWORD': '123poznavayka',
       'HOST': 'localhost',
       'PORT': '',
   }
}
