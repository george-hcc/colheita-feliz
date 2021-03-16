from ._base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ewj$%1k+9n@d#8qz=3fa6ie3#ni3wq)n&_z=2h@8s^%45cj06o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
