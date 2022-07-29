from pathlib import Path

# SECURITY WARNING: keep the secret key used in production secret!
mySECRET_KEY = 'django-insecure-s-!ly69k6v9@xh2w)!79^j-92tgq$x=u@ml6)c!yj$c6!7@b!$'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

myDATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'QOL',
        'USER': 'root',
        'PASSWORD': 'Pqlamz000!',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}