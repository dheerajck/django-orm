import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# SECURITY WARNING: Modify this secret key if using in production!
SECRET_KEY = "6few3nci_q_o@l1dlbk81%wcxe!*6r29yu629&d97!hiqat9fa"

DEFAULT_AUTO_FIELD = 'django_orm.db.models.AutoField'

DATABASES = {
    "default": {
        "ENGINE": "django_orm.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


LANGUAGE_CODE = "en-us"
"""
To connect to an existing postgres database, first:
pip install psycopg2
then overwrite the settings above with:

DATABASES = {
    'default': {
        'ENGINE': 'django_orm.db.backends.postgresql_psycopg2',
        'NAME': 'name',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
"""

INSTALLED_APPS = ("example",)
