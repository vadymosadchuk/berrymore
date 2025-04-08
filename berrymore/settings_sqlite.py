"""
Django settings for berrymore project.

Altered for sqlite.
"""

from .settings import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'TEST': {
            'NAME': 'mytestdatabase',
        },
    }
}
